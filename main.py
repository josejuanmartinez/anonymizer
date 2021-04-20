import logging

import aiohttp_cors as aiohttp_cors
from aiohttp import web
from endpoints.routes import routes

logging.basicConfig(level=logging.INFO)


app = web.Application()
app.add_routes(routes)
cors = aiohttp_cors.setup(app, defaults={
            "*": aiohttp_cors.ResourceOptions(
                allow_credentials=True,
                expose_headers="*",
                allow_methods="*",
                allow_headers="*",
                max_age=3600
            )
        })

for route in app.router.routes():
    logging.info(f'Adding cors to {route.method} {route.handler}')
    cors.add(route)

if __name__ == '__main__':
    web.run_app(app, port=9090)
