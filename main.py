import logging
import json
import time
from datetime import datetime
from ai_predictor import AiPredictor
from risk_manager import RiskManager
from exchange_connector import ExchangeConnector

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('trading_bot.log'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)

class CryptoTradingBot:
    """Main trading bot class that orchestrates AI predictions and trading execution."""
    
    def __init__(self, config_path='config.json'):
        """Initialize the trading bot with configuration."""
        self.config = self.load_config(config_path)
        self.ai_predictor = AiPredictor(self.config)
        self.risk_manager = RiskManager(self.config)
        self.exchange = ExchangeConnector(self.config)
        self.is_running = False
        logger.info("CryptoTradingBot initialized successfully")
    
    def load_config(self, config_path):
        """Load configuration from JSON file."""
        try:
            with open(config_path, 'r') as f:
                config = json.load(f)
            logger.info(f"Configuration loaded from {config_path}")
            return config
        except FileNotFoundError:
            logger.error(f"Configuration file {config_path} not found")
            raise
        except json.JSONDecodeError:
            logger.error(f"Invalid JSON in configuration file {config_path}")
            raise
    
    def analyze_market(self, symbol):
        """Analyze market conditions for a given trading pair."""
        logger.info(f"Analyzing market for {symbol}")
        market_data = self.exchange.get_market_data(symbol)
        ai_prediction = self.ai_predictor.predict(market_data)
        return ai_prediction
    
    def execute_trade(self, symbol, prediction, market_data):
        """Execute trade based on AI prediction and risk management rules."""
        logger.info(f"Evaluating trade for {symbol}")
        
        # Check risk parameters
        if not self.risk_manager.validate_trade(symbol, prediction, market_data):
            logger.warning(f"Trade validation failed for {symbol}")
            return False
        
        # Calculate position size
        position_size = self.risk_manager.calculate_position_size(
            market_data['price'],
            self.config['risk_per_trade']
        )
        
        # Execute the trade
        if prediction['signal'] == 'BUY':
            order = self.exchange.place_buy_order(symbol, position_size)
            logger.info(f"BUY order placed for {symbol}: {order}")
        elif prediction['signal'] == 'SELL':
            order = self.exchange.place_sell_order(symbol, position_size)
            logger.info(f"SELL order placed for {symbol}: {order}")
        
        return True
    
    def monitor_positions(self):
        """Monitor open positions and manage stops/targets."""
        logger.info("Monitoring open positions")
        positions = self.exchange.get_positions()
        
        for position in positions:
            current_price = self.exchange.get_current_price(position['symbol'])
            self.risk_manager.update_position(position, current_price)
    
    def run(self):
        """Main trading loop."""
        self.is_running = True
        logger.info("Starting trading bot...")
        
        try:
            while self.is_running:
                for symbol in self.config['trading_pairs']:
                    try:
                        # Analyze market
                        prediction = self.analyze_market(symbol)
                        
                        # Get current market data
                        market_data = self.exchange.get_market_data(symbol)
                        
                        # Execute trade if signal is strong enough
                        if prediction['confidence'] > self.config['min_confidence']:
                            self.execute_trade(symbol, prediction, market_data)
                        else:
                            logger.info(f"Confidence too low for {symbol}: {prediction['confidence']}")
                    
                    except Exception as e:
                        logger.error(f"Error trading {symbol}: {str(e)}")
                
                # Monitor existing positions
                self.monitor_positions()
                
                # Sleep before next iteration
                time.sleep(self.config['update_interval'])
        
        except KeyboardInterrupt:
            logger.info("Trading bot interrupted by user")
        except Exception as e:
            logger.error(f"Fatal error in trading loop: {str(e)}")
        finally:
            self.stop()
    
    def stop(self):
        """Stop the trading bot."""
        self.is_running = False
        logger.info("Trading bot stopped")

if __name__ == '__main__':
    bot = CryptoTradingBot('config.json')
    bot.run()