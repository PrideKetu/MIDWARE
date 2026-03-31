from connectors.restconnect import handle_rest

def route_request(request):
    # simple logic for now
    if request.path.startswith('/api/test'):
        return handle_rest(request)
    
    return {"error": "No route found"}