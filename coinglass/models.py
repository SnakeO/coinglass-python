"""
CoinGlass API Response Models
Pydantic models for API response validation and typing
"""
from typing import Optional, List, Dict, Any, Union
from datetime import datetime
from pydantic import BaseModel, Field, validator


class BaseResponse(BaseModel):
    """Base response model for all CoinGlass API responses."""
    code: str
    msg: str
    data: Any
    
    @validator('code')
    def validate_success(cls, v, values):
        """Validate that the response indicates success."""
        if v != '0':
            raise ValueError(f"API returned error code: {v}")
        return v


class CoinMarketData(BaseModel):
    """Market data for a cryptocurrency."""
    symbol: str
    current_price: float
    price_change_percent_24h: Optional[float] = None
    market_cap_usd: Optional[float] = None
    volume_usd: Optional[float] = None
    open_interest_usd: Optional[float] = None
    open_interest_quantity: Optional[float] = None
    avg_funding_rate_by_oi: Optional[float] = None
    avg_funding_rate_by_vol: Optional[float] = None
    open_interest_market_cap_ratio: Optional[float] = None
    open_interest_volume_ratio: Optional[float] = None
    open_interest_change_percent_24h: Optional[float] = None
    volume_change_percent_24h: Optional[float] = None
    volume_change_usd_24h: Optional[float] = None
    long_short_ratio_24h: Optional[float] = None
    liquidation_usd_24h: Optional[float] = None
    long_liquidation_usd_24h: Optional[float] = None
    short_liquidation_usd_24h: Optional[float] = None


class PairMarketData(BaseModel):
    """Market data for a trading pair."""
    instrument_id: str
    exchange_name: str
    symbol: str
    current_price: float
    index_price: Optional[float] = None
    price_change_percent_24h: Optional[float] = None
    volume_usd: Optional[float] = None
    volume_usd_change_percent_24h: Optional[float] = None
    long_volume_usd: Optional[float] = None
    short_volume_usd: Optional[float] = None
    long_volume_quantity: Optional[float] = None
    short_volume_quantity: Optional[float] = None
    open_interest_quantity: Optional[float] = None
    open_interest_usd: Optional[float] = None
    open_interest_change_percent_24h: Optional[float] = None
    long_liquidation_usd_24h: Optional[float] = None
    short_liquidation_usd_24h: Optional[float] = None
    funding_rate: Optional[float] = None
    next_funding_time: Optional[int] = None
    open_interest_volume_ratio: Optional[float] = None
    oi_vol_ratio_change_percent_24h: Optional[float] = None


class OHLCData(BaseModel):
    """OHLC (Open, High, Low, Close) data point."""
    time: int  # Unix timestamp in milliseconds
    open: Union[str, float]
    high: Union[str, float]
    low: Union[str, float]
    close: Union[str, float]
    volume_usd: Optional[Union[str, float]] = None
    
    @validator('open', 'high', 'low', 'close', 'volume_usd', pre=True)
    def convert_to_float(cls, v):
        """Convert string values to float."""
        if v is None:
            return v
        if isinstance(v, str):
            return float(v)
        return v


class LiquidationData(BaseModel):
    """Liquidation data point."""
    time: int
    long_liquidation_usd: Union[str, float]
    short_liquidation_usd: Union[str, float]
    
    @validator('long_liquidation_usd', 'short_liquidation_usd', pre=True)
    def convert_to_float(cls, v):
        """Convert string values to float."""
        if isinstance(v, str):
            return float(v)
        return v


class FundingRateData(BaseModel):
    """Funding rate data for an exchange."""
    exchange: str
    funding_rate: float
    cumulative_funding_rate: Optional[float] = None


class OpenInterestData(BaseModel):
    """Open interest data point."""
    time: int
    open: Union[str, float]
    high: Union[str, float]
    low: Union[str, float]
    close: Union[str, float]
    
    @validator('open', 'high', 'low', 'close', pre=True)
    def convert_to_float(cls, v):
        """Convert string values to float."""
        if isinstance(v, str):
            return float(v)
        return v


class ExchangeRankData(BaseModel):
    """Exchange ranking data."""
    exchange: str
    open_interest_usd: float
    volume_usd: float
    market_share_percent: float


class MaxPainData(BaseModel):
    """Options max pain data."""
    date: str
    call_open_interest: float
    put_open_interest: float
    call_open_interest_market_value: float
    put_open_interest_market_value: float
    max_pain_price: str
    call_open_interest_notional: float
    put_open_interest_notional: float


class ETFData(BaseModel):
    """ETF data."""
    ticker: str
    name: str
    net_assets: Optional[float] = None
    premium_discount: Optional[float] = None
    daily_flow: Optional[float] = None


class ExchangeAssetData(BaseModel):
    """Exchange on-chain asset data."""
    symbol: str
    assets_name: str
    price: float
    reserve_quantity: float
    reserve_usd: float


class EconomicEventData(BaseModel):
    """Economic calendar event data."""
    date: str
    time: str
    event: str
    forecast: Optional[Union[str, float]] = None
    previous: Optional[Union[str, float]] = None
    actual: Optional[Union[str, float]] = None


class FearGreedData(BaseModel):
    """Fear and Greed Index data."""
    time: int
    value: float
    classification: str


class BitcoinIndicatorData(BaseModel):
    """Bitcoin-specific indicator data."""
    time: Optional[int] = None
    value: float
    indicator_name: Optional[str] = None
    status: Optional[str] = None