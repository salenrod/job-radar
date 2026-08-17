# Configuracao do perfil INTERNACIONAL do JobRadar.
#
# Objetivo deste perfil:
# - vagas 100% remotas fora do Brasil;
# - foco em Cloud Security, Detection Engineering, SOC/SecOps, SIEM,
#   Threat Hunting e Incident Response;
# - aceitar anuncios em ingles, portugues ou espanhol;
# - rejeitar vagas que declarem explicitamente um mercado incompatível
#   (por exemplo: "Remote - US only" ou "Remote - India").
#
# Mantemos os nomes das variaveis esperados por perfis.py/job.py para nao
# quebrar a arquitetura original do projeto.

from config import (
    TELEGRAM_BOT_TOKEN,
    TELEGRAM_CHAT_ID,
    DB_PATH,
    CIDADES_EUROPA_IBERICA,
)  # noqa: F401


# -----------------------------------------------------------------------------
# CARGOS INTERNACIONAIS
# -----------------------------------------------------------------------------
# IMPORTANTE: no perfil internacional atual, perfis.py envia TODA esta lista
# como `keywords_forte`. Portanto, entram aqui apenas titulos suficientemente
# especificos. Cargos genericos como "Security Analyst" e "Security Engineer"
# ficam de fora para evitar vagas de GRC, IAM, AppSec, Vulnerability Management
# ou outras subareas que nao sao o foco deste radar.
KEYWORDS_INTL = [
    # Cloud Security
    "Cloud Security Engineer",
    "Cloud Security Analyst",
    "Cloud Security Specialist",
    "Cloud Detection Engineer",

    # Detection Engineering / Detection & Response
    "Detection Engineer",
    "Security Detection Engineer",
    "Threat Detection Engineer",
    "Detection and Response Engineer",
    "Security Detection and Response Engineer",

    # Security Operations / SOC / SecOps
    "Security Operations Engineer",
    "Security Operations Analyst",
    "Security Operations Center Analyst",
    "SOC Analyst",
    "SOC Engineer",
    "SecOps Engineer",

    # SIEM / Monitoring
    "SIEM Engineer",
    "SIEM Analyst",
    "Security Monitoring Engineer",
    "Security Monitoring Analyst",

    # Threat Hunting / Incident Response / Cyber Defense
    "Threat Hunter",
    "Threat Hunting Analyst",
    "Incident Response Engineer",
    "Incident Response Analyst",
    "Cyber Defense Engineer",
    "Cyber Defense Analyst",
    "Cyber Defence Engineer",
    "Cyber Defence Analyst",
    "Blue Team Engineer",
    "Blue Team Analyst",

    # Portugues - Portugal / empresas internacionais que anunciam em PT
    "Engenheiro de Seguranca em Nuvem",
    "Analista de Seguranca em Nuvem",
    "Engenheiro de Seguranca Cloud",
    "Analista de Seguranca Cloud",
    "Engenheiro de Deteccao",
    "Analista de Deteccao",
    "Analista SOC",
    "Engenheiro SOC",
    "Analista SIEM",
    "Engenheiro SIEM",
    "Analista de Resposta a Incidentes",
    "Engenheiro de Resposta a Incidentes",

    # Espanhol - Espanha / LATAM
    "Ingeniero de Seguridad en la Nube",
    "Analista de Seguridad en la Nube",
    "Ingeniero de Seguridad Cloud",
    "Analista de Seguridad Cloud",
    "Ingeniero de Ciberseguridad Cloud",
    "Analista de Ciberseguridad Cloud",
    "Ingeniero de Deteccion",
    "Analista de Deteccion",
    "Ingeniero SOC",
    "Ingeniero SIEM",
    "Ingeniero de Respuesta a Incidentes",
    "Analista de Respuesta a Incidentes",
]


# -----------------------------------------------------------------------------
# TERMOS DE BUSCA
# -----------------------------------------------------------------------------
# Estes termos sao enviados aos scrapers. O filtro final continua sendo o
# titulo da vaga contra KEYWORDS_INTL, entao termos de stack podem ampliar o
# recall sem, sozinhos, aprovar uma vaga irrelevante.
TERMOS_BUSCA_INTL = [
    # Cargos principais em ingles
    "cloud security engineer",
    "cloud security analyst",
    "cloud detection engineer",
    "detection engineer",
    "threat detection engineer",
    "detection and response engineer",
    "security operations engineer",
    "security operations analyst",
    "soc analyst",
    "soc engineer",
    "siem engineer",
    "siem analyst",
    "threat hunter",
    "threat hunting analyst",
    "incident response engineer",
    "incident response analyst",
    "cyber defense analyst",
    "blue team engineer",

    # Cloud / SIEM / Detection stack
    "aws security engineer",
    "azure security engineer",
    "cloud security aws",
    "cloud security azure",
    "microsoft sentinel security",
    "splunk security",
    "qradar security",
    "defender xdr security",
    "security operations siem",
    "detection engineering siem",
    "threat detection cloud",
    "threat hunting siem",

    # Mercado remoto / LATAM - aumenta recall para vagas regionais
    "cloud security latam",
    "detection engineer latam",
    "security operations latam",
    "soc analyst latam",
    "cloud security latin america",
    "detection engineer latin america",

    # Portugues
    "engenheiro de seguranca cloud",
    "seguranca em nuvem",
    "engenheiro de deteccao",
    "analista soc remoto",
    "analista siem remoto",
    "resposta a incidentes",

    # Espanhol
    "ingeniero de seguridad cloud",
    "seguridad en la nube",
    "ingeniero de deteccion",
    "respuesta a incidentes",
]


# O JobRadar roda os termos em blocos e guarda o offset no jobs.db.
# Com ~50 termos, bloco 10 cobre toda a lista em aproximadamente 5 ciclos,
# sem multiplicar demais o custo de cada execucao (cada termo roda por pais).
TERMOS_POR_CICLO_INTL = 10


# -----------------------------------------------------------------------------
# IDIOMA / REMOTO GLOBAL
# -----------------------------------------------------------------------------
# O config_intl.py original exigia espanhol/portugues/LATAM no TITULO quando
# uma vaga remota nao declarava mercado geografico. Isso fazia sentido para o
# objetivo original, mas elimina vagas internacionais em ingles que sao
# realmente Worldwide/Anywhere ou cujo card nao declara pais.
#
# RegrasFiltro aceita None: nesse modo nao existe gate de idioma. O gate de
# mercado continua ativo logo abaixo atraves de MERCADOS_REMOTO_ACEITOS_INTL,
# portanto "Remote - US only" e mercados explicitamente incompatíveis seguem
# rejeitados. Apenas remoto sem restricao geografica declarada deixa de ser
# descartado por nao dizer "Spanish"/"Portuguese" no titulo.
IDIOMAS_EXIGIDOS_INTL = None


# -----------------------------------------------------------------------------
# ONDE PESQUISAR
# -----------------------------------------------------------------------------
# LinkedInIntlScraper multiplica termos x locations. Mantemos LATAM + Iberia
# como mercados de busca direta, evitando EUA/Reino Unido como location porque
# isso tende a gerar grande volume de vagas locais/US-only que depois seriam
# descartadas pelo filtro de mercado.
#
# Vagas realmente Worldwide/Anywhere ainda podem entrar por fontes remotas como
# WeWorkRemotely e por resultados sem restricao geografica explicita.
LOCATIONS_INTL = [
    "Spain",
    "Portugal",
    "Mexico",
    "Colombia",
    "Argentina",
    "Chile",
]


# Perfil internacional principal: apenas remoto.
CIDADES_INTL = ["Remote", "Remoto"]


# -----------------------------------------------------------------------------
# MERCADOS REMOTOS ACEITOS
# -----------------------------------------------------------------------------
# Esta e uma allowlist para vagas que DECLARAM explicitamente o mercado.
# Nao inclui Brasil porque o perfil `brasil` ja cobre esse mercado.
# Nao inclui Estados Unidos/Reino Unido/India etc. para nao aprovar vaga
# regional que exija estar naquele pais.
#
# Worldwide / Anywhere / Global sao tratados pelo job.py como "sem restricao"
# e, portanto, nao precisam aparecer nesta lista.
MERCADOS_REMOTO_ACEITOS_INTL = [
    "Portugal",
    "Espanha",
    "México",
    "Colômbia",
    "Argentina",
    "Chile",
    "Peru",
    "Uruguai",
    "Paraguai",
    "Bolívia",
    "Equador",
    "Venezuela",
    "Costa Rica",
    "Panamá",
    "Guatemala",
    "Honduras",
    "El Salvador",
    "Nicarágua",
    "República Dominicana",
    "Porto Rico",
    "Cuba",
    "Angola",
    "Moçambique",
    "Cabo Verde",
    "LATAM",
]


# Presencial/hibrido em Portugal/Espanha continua desligado. O objetivo deste
# perfil e remoto internacional; para habilitar o eixo exploratorio iberico,
# mude para True.
ATIVAR_EIXO_IBERICO = False


# -----------------------------------------------------------------------------
# INDEED INTERNACIONAL
# -----------------------------------------------------------------------------
# IndeedIntlScraper usa subdominios por pais. Mantemos os mesmos seis mercados
# do escopo internacional atual para evitar ampliar custo/ruido sem necessidade.
DOMINIOS_INDEED_INTL = {
    "Espanha": "es.indeed.com",
    "Portugal": "pt.indeed.com",
    "México": "mx.indeed.com",
    "Colômbia": "co.indeed.com",
    "Argentina": "ar.indeed.com",
    "Chile": "cl.indeed.com",
}
