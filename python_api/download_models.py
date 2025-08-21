import ssl
import nltk

# This part creates a special "unverified" SSL context
# and tells Python to use it for downloads.
try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

print("--- Step 1: Attempting to download NLTK data ---")
try:
    # Download each package individually for better error tracking
    print("Downloading 'punkt'...")
    nltk.download('punkt')
    print("Downloading 'wordnet'...")
    nltk.download('wordnet')
    print("Downloading 'omw-1.4'...")
    nltk.download('omw-1.4')
    print("\n✅ NLTK data downloaded successfully.")
except Exception as e:
    print(f"\n❌ Failed to download NLTK data. Error: {e}")
    print("This may be due to a network firewall. Please proceed to Step 2 regardless.")
