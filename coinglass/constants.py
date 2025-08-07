"""
Constants and enums for CoinGlass API
"""

# Plan Level System (1-5)
class PlanLevel:
    """API Plan levels with numeric hierarchy"""
    HOBBYIST = 1       # Level 1: Hobbyist plan
    STARTUP = 2        # Level 2: Startup plan
    STANDARD = 3       # Level 3: Standard plan
    PROFESSIONAL = 4   # Level 4: Professional plan
    ENTERPRISE = 5     # Level 5: Enterprise plan
    
    # Mappings for display and conversion
    LEVEL_TO_NAME = {
        1: "Hobbyist",
        2: "Startup",
        3: "Standard", 
        4: "Professional",
        5: "Enterprise"
    }
    
    NAME_TO_LEVEL = {
        "Hobbyist": 1,
        "Startup": 2,
        "Standard": 3,
        "Professional": 4,
        "Enterprise": 5
    }
    
    @classmethod
    def get_name(cls, level: int) -> str:
        """Get plan name from level number."""
        return cls.LEVEL_TO_NAME.get(level, f"Level {level}")
    
    @classmethod
    def get_level(cls, name: str) -> int:
        """Get level number from plan name."""
        return cls.NAME_TO_LEVEL.get(name, 1)
    
    @classmethod
    def meets_requirement(cls, user_level: int, required_level: int) -> bool:
        """Check if user's plan level meets the requirement."""
        return user_level >= required_level

# Legacy support - will be removed in future versions
class PlanTier:
    """DEPRECATED: Use PlanLevel instead. API Plan tiers with hierarchy"""
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