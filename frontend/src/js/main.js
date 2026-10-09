document.addEventListener('DOMContentLoaded', () => {
    const consentView = document.getElementById('consent-view');
    const dashboardView = document.getElementById('dashboard-view');
    
    const btnAccept = document.getElementById('btn-accept');
    const btnDecline = document.getElementById('btn-decline');
    const btnReset = document.getElementById('btn-reset');
    
    const ipResultsPanel = document.getElementById('ip-results');
    const ipDataPre = document.getElementById('ip-data');
    const scenarioDataPre = document.getElementById('scenario-data');

    function showDashboard() {
        consentView.classList.remove('active');
        dashboardView.classList.add('active');
    }

    function resetApp() {
        dashboardView.classList.remove('active');
        consentView.classList.add('active');
        ipResultsPanel.classList.add('hidden');
        ipDataPre.textContent = 'Carregando...';
        scenarioDataPre.textContent = 'Carregando...';
    }

    async function loadScenarios() {
        const scenarios = await fetchScenarios();
        if (scenarios && scenarios.length > 0) {
            scenarioDataPre.textContent = JSON.stringify(scenarios[0], null, 2);
        } else {
            scenarioDataPre.textContent = "Nenhum cenário encontrado.";
        }
    }

    btnAccept.addEventListener('click', async () => {
        showDashboard();
        ipResultsPanel.classList.remove('hidden');
        
        // Fetch IP Data
        const ipData = await fetchIpData();
        ipDataPre.textContent = JSON.stringify(ipData, null, 2);
        
        // Fetch Scenario
        await loadScenarios();
    });

    btnDecline.addEventListener('click', async () => {
        showDashboard();
        // Oculta painel de IP pois usuário recusou
        ipResultsPanel.classList.add('hidden');
        
        // Carrega apenas cenários
        await loadScenarios();
    });

    btnReset.addEventListener('click', resetApp);
});
