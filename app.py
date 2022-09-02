import time

from flask import Flask, render_template
import fuel_prices
import local_test

app = Flask(__name__)

init_stations = fuel_prices.get_prices()
last_refresh = time.time()
#print(stations)
#stations = local_test.get_local_price()
#test_data = "test"


@app.route('/refreshprices')
def refreshprices():
    time_diff = time.time() - last_refresh
    if time_diff > 300:
        stations = fuel_prices.get_prices()
        return overview(stations)
    else:
        return render_template("overview.html", stations=init_stations, warning=True, warntime=300 - int(time_diff))



@app.route('/')
def overview(stations=init_stations):
    return render_template("overview.html", stations=stations)


if __name__ == '__main__':
    app.run(port=5001)
