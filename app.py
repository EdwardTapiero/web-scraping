from flask import Flask, jsonify, request

from core.const import RESET_SEARCH, PAGINATION, BRAND, HOST, PORT
from service.functions import verify_reset

app = Flask(__name__)


@app.route('/api/v1/mercado_libre/consulta_marca', methods=["GET"])
def mercado_libre():
    print("Started service")

    args = request.args

    reset = args.get("reset", default=RESET_SEARCH, type=bool)
    pag = args.get("pagination", default=PAGINATION, type=int)
    brand = args.get("brand", default=BRAND, type=str)

    count_brand = verify_reset(reset, pag, brand)

    print("Leaving service")

    return jsonify({"Datos": {"Marca": brand, "Paginas buscadas": pag, "Registros encontrados por marca": count_brand,
                              "Nueva busqueda": reset}})


if __name__ == "__main__":
    app.run(host=HOST, debug=True, port=PORT)
