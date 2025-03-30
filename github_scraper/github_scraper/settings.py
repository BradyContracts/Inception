# settings.py

# Enable Scrapy-Splash
SPLASH_URL = 'http://localhost:8050'  # URL where Splash service is running

# Middleware settings
DOWNLOADER_MIDDLEWARES = {
   'scrapy_splash.SplashMiddleware': 725,  # Enables Splash middleware
   'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware': 810,  # For gzip, deflate
}

# Spider middleware settings
SPIDER_MIDDLEWARES = {
   'scrapy_splash.SplashSpiderMiddleware': 725,  # Enables Spider middleware for Splash
}

# Enable Splash to render JS content
DUPEFILTER_CLASS = 'scrapy_splash.dupefilter.SplashAwareDupeFilter'
HTTPCACHE_STORAGE = 'scrapy_splash.persistences.SplashAwareFSCacheStorage'  # Cache for rendered pages

# Cache settings for Splash (optional, but speeds up repeated requests)
HTTPCACHE_ENABLED = True
HTTPCACHE_EXPIRATION_SECS = 3600  # Cache expiry time in seconds
HTTPCACHE_DIR = 'httpcache'  # Cache directory

# Configure the logging level
LOG_LEVEL = 'DEBUG'

# Set the download delay to avoid overloading the server (adjust to your needs)
DOWNLOAD_DELAY = 1  # Delay between requests in seconds

# Scrapy settings (optional)
CONCURRENT_REQUESTS = 16  # Number of concurrent requests
CONCURRENT_REQUESTS_PER_DOMAIN = 8  # Requests per domain
DOWNLOAD_TIMEOUT = 180  # Timeout for page load

# Splash-specific settings
# Set the arguments for Splash (can adjust the wait time for JS to load)
SPLASH_COOKIES_DEBUG = True  # Optional: Enables logging of cookies in Splash
