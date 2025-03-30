import scrapy
import requests
import json
import os
from dotenv import load_dotenv

# Load GitHub API token
load_dotenv()
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

class GithubApiSpider(scrapy.Spider):
    name = "github_api"
    allowed_domains = ["api.github.com"]
    
    def start_requests(self):
        """Start with a search query for repositories"""
        url = "https://api.github.com/search/repositories?q=language:python&sort=stars&per_page=5"
        headers = {"Authorization": f"token {GITHUB_TOKEN}"}
        yield scrapy.Request(url, headers=headers, callback=self.parse_repos)

    def parse_repos(self, response):
        """Extract repository details and request code files"""
        data = json.loads(response.text)
        for repo in data["items"]:
            repo_name = repo["full_name"]
            repo_url = repo["url"]
            contents_url = f"https://api.github.com/repos/{repo_name}/contents"
            headers = {"Authorization": f"token {GITHUB_TOKEN}"}
            yield scrapy.Request(contents_url, headers=headers, callback=self.parse_contents, meta={"repo_name": repo_name})

    def parse_contents(self, response):
        """Extract Python files from the repository"""
        repo_name = response.meta["repo_name"]
        data = json.loads(response.text)
        
        for file in data:
            if file["type"] == "file" and file["name"].endswith(".py"):
                yield {
                    "repo": repo_name,
                    "file_name": file["name"],
                    "download_url": file["download_url"]
                }
