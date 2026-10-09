from fastapi import APIRouter, HTTPException, Request
from app.services.scenarios import get_all_scenarios, get_scenario_by_id, mock_ip_lookup

router = APIRouter()

@router.get("/health")
def health_check():
    return {"status": "ok"}

@router.get("/v1/scenarios")
def list_scenarios():
    return get_all_scenarios()

@router.get("/v1/scenarios/{scenario_id}")
def get_scenario(scenario_id: str):
    scenario = get_scenario_by_id(scenario_id)
    if not scenario:
        raise HTTPException(status_code=404, detail="Cenário não encontrado")
    return scenario

@router.get("/v1/ip-lookup")
def get_ip_geolocation(request: Request):
    # Obtém IP do cliente (simulado para testes locais e fins educativos)
    client_ip = request.client.host if request.client else "127.0.0.1"
    return mock_ip_lookup(client_ip)
