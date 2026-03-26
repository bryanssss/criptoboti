# Risk Management Module

"""
This module controls position sizing, stop-loss management, and overall portfolio risk. 
It includes functions to calculate position size, validate trades, manage open positions, 
calculate drawdown, and maintain portfolio statistics.
"""

class RiskManager:
    def __init__(self, account_equity):
        self.account_equity = account_equity
        self.open_positions = []
        self.trade_history = []

    def calculate_position_size(self, risk_percent, entry_price, stop_loss_price):
        risk_amount = self.account_equity * (risk_percent / 100)
        position_size = risk_amount / abs(entry_price - stop_loss_price)
        return position_size

    def validate_trade(self, position_size, entry_price, stop_loss_price):
        if position_size <= 0:
            raise ValueError('Position size must be greater than 0')
        if stop_loss_price >= entry_price:
            raise ValueError('Stop-loss price must be below entry price')

    def manage_open_positions(self, position_size, entry_price, stop_loss_price):
        self.validate_trade(position_size, entry_price, stop_loss_price)
        self.open_positions.append({'size': position_size, 'entry_price': entry_price, 'stop_loss': stop_loss_price})

    def calculate_drawdown(self):
        if not self.trade_history:
            return 0
        peak = max(self.trade_history)
        trough = min(self.trade_history)
        return (peak - trough) / peak * 100

    def record_trade(self, profit_loss):
        self.trade_history.append(profit_loss)

    def portfolio_statistics(self):
        total_trades = len(self.trade_history)
        total_profit = sum(self.trade_history)
        win_rate = len([p for p in self.trade_history if p > 0]) / total_trades if total_trades > 0 else 0
        return {
            'total_trades': total_trades,
            'total_profit': total_profit,
            'win_rate': win_rate,
        }