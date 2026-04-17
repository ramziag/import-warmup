from portfolio.data import create_portfolio
import portfolio.report

my_portfolio = portfolio.data.create_portfolio("Retirement")
portfolio.report.print_report(my_portfolio)