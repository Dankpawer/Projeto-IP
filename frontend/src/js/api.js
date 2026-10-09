const API_BASE_URL = 'http://localhost:8000/api/v1';

async function fetchIpData() {
    try {
        const response = await fetch(`${API_BASE_URL}/ip-lookup`);
        if (!response.ok) throw new Error('Falha na API');
        return await response.json();
    } catch (error) {
        console.error("Erro ao buscar IP:", error);
        return { error: "Não foi possível carregar os dados de IP." };
    }
}

async function fetchScenarios() {
    try {
        const response = await fetch(`${API_BASE_URL}/scenarios`);
        if (!response.ok) throw new Error('Falha na API');
        return await response.json();
    } catch (error) {
        console.error("Erro ao buscar cenários:", error);
        return [{ error: "Não foi possível carregar os cenários." }];
    }
}
