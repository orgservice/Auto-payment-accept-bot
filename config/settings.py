import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    # Telegram Configuration
    API_ID = int(os.getenv('API_ID', '29158577'))
    API_HASH = os.getenv('API_HASH', '5a31bb001fafce5f0c8669b0a8138280')
    BOT_TOKEN = os.getenv('BOT_TOKEN', '8445776517:AAFACN-ITibKhAKgrxD3IgSXlvA3RZKq5c4')
    OWNER_ID = int(os.getenv('OWNER_ID', '5442514242'))
    
    # Database Configuration
    DB_URL = os.getenv('DB_URL', 'postgres://koyeb-adm:npg_kZQ2O4GVqWmT@ep-rough-frog-agawds6u.c-2.eu-central-1.pg.koyeb.app/koyebdb')
    
    # Group/Channel IDs
    GROUP_ID = int(os.getenv('GROUP_ID', '-1003350550618'))
    CHANNEL_ID = int(os.getenv('CHANNEL_ID', '-1003386923017'))
    
    # Payment Verification
    PAYMENT_VERIFICATION_TIMEOUT = int(os.getenv('PAYMENT_VERIFICATION_TIMEOUT', 300))  # 5 minute
    
    # Logging Configuration
    LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')
    
    @property
    def DATABASE_CONFIG(self):
        return {
            'connections': {
                'default': self.DB_URL
            },
            'apps': {
                'models': {
                    'models': ['database.models', 'aerich.models'],
                    'default_connection': 'default',
                }
            }
        }

settings = Settings()
