"""
Constants and enums for CoinGlass API
"""

class PlanTier:
    """API Plan tiers with hierarchy: Hobbyist -> Startup -> Standard -> Professional -> Enterprise"""
    HOBBYIST = "Hobbyist"
    STARTUP = "Startup" 
    STANDARD = "Standard"
    PROFESSIONAL = "Professional"
    ENTERPRISE = "Enterprise"
    ALL = "All plans"
    
    # Shorthand versions for docstrings
    STARTUP_PLUS = "Startup+"  # Startup and above
    STANDARD_PLUS = "Standard+"  # Standard and above
    PROFESSIONAL_PLUS = "Professional+"  # Professional and above

class Interval:
    """Valid interval values for time series data"""
    ONE_MIN = "1m"
    THREE_MIN = "3m"
    FIVE_MIN = "5m"
    FIFTEEN_MIN = "15m"
    THIRTY_MIN = "30m"
    ONE_HOUR = "1h"
    FOUR_HOUR = "4h"
    SIX_HOUR = "6h"
    EIGHT_HOUR = "8h"
    TWELVE_HOUR = "12h"
    ONE_DAY = "1d"
    ONE_WEEK = "1w"
    
    # All valid intervals
    ALL = [ONE_MIN, THREE_MIN, FIVE_MIN, FIFTEEN_MIN, THIRTY_MIN, 
           ONE_HOUR, FOUR_HOUR, SIX_HOUR, EIGHT_HOUR, TWELVE_HOUR,
           ONE_DAY, ONE_WEEK]
    
    # Intervals for specific endpoints
    FUNDING_RATE = [EIGHT_HOUR]  # Funding rate specific
    LONG_SHORT_RATIO = [FIVE_MIN, FIFTEEN_MIN, THIRTY_MIN, ONE_HOUR, FOUR_HOUR, ONE_DAY]
    EXCHANGE_HISTORY_CHART = [ONE_HOUR, FOUR_HOUR, ONE_DAY]

class TransactionType:
    """Transaction types for on-chain data"""
    IN = "in"
    OUT = "out"

class Importance:
    """Economic calendar event importance levels"""
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"

class Currency:
    """Common currency types"""
    USD = "USD"
    USDT = "USDT"
    BTC = "BTC"
    ETH = "ETH"

class TimeType:
    """Time type options for options data"""
    DAILY = "1d"
    WEEKLY = "1w"
    MONTHLY = "1m"

# Common parameter defaults
DEFAULT_LIMIT = 100
MAX_LIMIT = 1000
MAX_LIMIT_SMALL = 100

# Cache times (in seconds)
class CacheTime:
    """Cache refresh rates for various endpoints"""
    REALTIME = "Real-time"
    ONE_SECOND = "Every 1 second"
    TEN_SECONDS = "Every 10 seconds"
    TWENTY_SECONDS = "Every 20 seconds"
    THIRTY_SECONDS = "Every 30 seconds"
    ONE_MINUTE = "Every 1 minute"
    ONE_HOUR = "Every 1 hour"
    DAILY = "Daily updates"