import os
from dotenv import load_dotenv

load_dotenv()

# -----------------------------------------------------------------------------
# PERFIL BRASIL - CLOUD SECURITY / DETECTION / SOC-SECOps
# -----------------------------------------------------------------------------
# Regra de desenho:
# - titulos muito especificos passam direto;
# - titulos genericos de Seguranca da Informacao tambem podem passar, porque
#   muitas empresas publicam "Analista/Engenheiro de Seguranca" e deixam SIEM,
#   Cloud, EDR e resposta a incidentes apenas na descricao;
# - subareas fora do objetivo (GRC, IAM puro, AppSec puro etc.) sao barradas
#   quando aparecem explicitamente no TITULO.

KEYWORDS_CARGO_FORTE = [
    # Cloud Security - inclui ordem PT/EN usada no mercado brasileiro
    "Cloud Security",
    "Cloud Security Engineer",
    "Cloud Security Analyst",
    "Cloud Security Specialist",
    "Analista de Cloud Security",
    "Engenheiro de Cloud Security",
    "Especialista de Cloud Security",
    "Especialista em Cloud Security",
    "Analista de Seguranca Cloud",
    "Engenheiro de Seguranca Cloud",
    "Analista de Seguranca em Nuvem",
    "Engenheiro de Seguranca em Nuvem",

    # Detection Engineering / Threat Detection
    "Detection Engineer",
    "Detection Engineering",
    "Security Detection Engineer",
    "Threat Detection Engineer",
    "Threat Detection",
    "Detection and Response Engineer",

    # SOC / SecOps / Security Operations
    "SOC Analyst",
    "Analista SOC",
    "Analista de SOC",
    "SOC Engineer",
    "Security Operations Analyst",
    "Security Operations Engineer",
    "Security Operations Center Analyst",
    "Security Operations",
    "SecOps Engineer",
    "SecOps Analyst",

    # SIEM / Monitoring
    "SIEM Engineer",
    "SIEM Analyst",
    "Engenheiro SIEM",
    "Analista SIEM",
    "Security Monitoring Engineer",
    "Security Monitoring Analyst",

    # Threat Hunting / Incident Response / Blue Team
    "Threat Hunter",
    "Threat Hunting Analyst",
    "Incident Response Engineer",
    "Incident Response Analyst",
    "Cyber Defense Engineer",
    "Cyber Defense Analyst",
    "Blue Team Engineer",
    "Blue Team Analyst",
]

# Cargos genericos. Eles existem em varias subareas, mas sao comuns em vagas
# defensivas boas. O job.py permite esses titulos SEM qualificador no proprio
# titulo, desde que nenhuma exclusao explicita abaixo apareca.
KEYWORDS_CARGO_AMBIGUO = [
    "Security Analyst",
    "Security Engineer",
    "Cyber Security Analyst",
    "Cybersecurity Analyst",
    "Cyber Security Engineer",
    "Cybersecurity Engineer",
    "Information Security Analyst",
    "Information Security Engineer",
    "Security Specialist",
    "Analista de Seguranca",
    "Analista de Seguranca da Informacao",
    "Analista de Ciberseguranca",
    "Engenheiro de Seguranca",
    "Engenheiro de Seguranca da Informacao",
    "Engenheiro de Ciberseguranca",
    "Especialista em Seguranca",
    "Especialista em Seguranca da Informacao",
]

# Se um cargo generico trouxer um destes termos no titulo, ganha o motivo
# "Cargo ambiguo + qualificador". Mantido com o nome legado esperado pelo
# projeto original.
QUALIFICADORES_DADOS = [
    "cloud", "nuvem", "aws", "azure", "gcp",
    "detection", "detecao", "soc", "secops", "security operations",
    "siem", "splunk", "sentinel", "qradar", "security monitoring", "monitoramento",
    "edr", "xdr", "defender", "crowdstrike", "threat", "ameaca", "hunting",
    "incident response", "resposta a incidentes", "dfir", "soar",
    "kql", "spl", "sigma", "mitre",
]

# Titulos genericos de seguranca sao rejeitados quando o TITULO declara que a
# funcao e principalmente uma trilha fora do objetivo deste radar. Evitamos
# palavras soltas como "risk" para nao bloquear um Detection Engineer que apenas
# mencione risco de forma incidental.
KEYWORDS_EXCLUSAO_TITULO = [
    "GRC",
    "Governance",
    "Governanca",
    "Compliance",
    "Conformidade",
    "IAM",
    "Identity and Access",
    "Identity Access",
    "Gestao de Acessos",
    "Application Security",
    "AppSec",
    "Product Security",
    "Pentest",
    "Penetration Tester",
    "Red Team",
    "Offensive Security",
    "Vulnerability Management",
    "Gestao de Vulnerabilidades",
    "Security Awareness",
    "Conscientizacao",
    "Privacy",
    "Privacidade",
    "TPRM",
    "Third Party Risk",
    "Auditoria",
    "Security Auditor",
]

# Permite "Analista/Engenheiro de Seguranca" mesmo quando SIEM/Cloud/etc.
# so aparecem na descricao da vaga. Isso corrige um falso negativo importante
# do modelo anterior, que via apenas o titulo do card do LinkedIn.
PERMITIR_CARGO_AMBIGUO_SEM_QUALIFICADOR = True

FERRAMENTAS_TITULO = [
    "Splunk", "Microsoft Sentinel", "Sentinel", "QRadar", "SIEM",
    "Defender XDR", "Microsoft Defender", "CrowdStrike", "EDR", "XDR",
]

QUALIFICADORES_CARGO = [
    "analista", "analyst", "engenheiro", "engineer", "especialista", "specialist",
    "arquiteto", "architect", "consultor", "consultant", "hunter",
]

KEYWORDS = KEYWORDS_CARGO_FORTE + KEYWORDS_CARGO_AMBIGUO

# -----------------------------------------------------------------------------
# BUSCA
# -----------------------------------------------------------------------------
# TERMOS_CORE rodam em TODO ciclo. O restante continua em rodizio para conter
# custo. Isso evita esperar ~12h para pesquisar de novo um titulo essencial.
TERMOS_CORE = [
    "analista de seguranca",
    "analista de seguranca da informacao",
    "engenheiro de seguranca",
    "cloud security",
    "security analyst",
    "security engineer",
    "soc analyst",
    "security operations",
    "detection engineer",
]

TERMOS_CARGO_EXTRA = [
    "cloud security",
    "detection engineering",
    "threat detection",
    "security operations",
    "soc cybersecurity",
    "siem security",
    "threat hunting",
]

TERMOS_CARGO = sorted(set(k.lower() for k in KEYWORDS) | set(TERMOS_CARGO_EXTRA))

TERMOS_FERRAMENTA = [
    "splunk security",
    "microsoft sentinel",
    "defender xdr",
    "qradar siem",
    "aws security",
    "azure security",
]

TERMOS_BUSCA = TERMOS_CARGO + TERMOS_FERRAMENTA
# Quantidade ROTATIVA por ciclo. Os TERMOS_CORE entram por fora desse limite.
TERMOS_POR_CICLO = 10

# -----------------------------------------------------------------------------
# LOCALIZACAO
# -----------------------------------------------------------------------------
CIDADES = [
    "Remoto",
    "Sao Paulo",
    "Campinas",
    "Barueri",
    "Rio de Janeiro",
    "Belo Horizonte",
    "Curitiba",
    "Florianopolis",
    "Porto Alegre",
    "Brasilia",
    "Recife",
]

CIDADES_EUROPA_IBERICA = [
    "Portugal", "Lisboa", "Porto", "Braga", "Espanha", "Espana", "Spain",
    "Madrid", "Barcelona", "Valencia",
]
ATIVAR_EIXO_IBERICO_BR = False

# O perfil Brasil agora busca apenas no Brasil. Antes ele repetia Argentina,
# Chile, Mexico, Colombia, Espanha e Portugal em TODA keyword, enquanto o perfil
# internacional fazia a mesma cobertura logo depois. A duplicacao aumentava
# muito a carga e o risco de rate-limit do LinkedIn.
LOCATIONS_LINKEDIN = ["Brasil"]
LOCATIONS_LINKEDIN_REMOTO_APENAS = []

# Uma vaga achada na busca brasileira pode declarar Brazil ou LATAM.
MERCADOS_REMOTO_ACEITOS = ["Brasil", "LATAM"]

# Mesma empresa+título pode ser uma NOVA abertura meses depois. URL/id continua
# deduplicando para sempre; chave secundaria so bloqueia repeticao recente.
JANELA_DEDUP_CHAVE_SECUNDARIA_DIAS = int(
    os.getenv("JANELA_DEDUP_CHAVE_SECUNDARIA_DIAS", 14)
)

# -----------------------------------------------------------------------------
# EXECUCAO / DIGEST / TELEGRAM
# -----------------------------------------------------------------------------
INTERVALO_MINUTOS = int(os.getenv("INTERVALO_MINUTOS", 180))
LIMIAR_DIGEST_IMEDIATO = 6
DIGEST_HORA_UTC = 0

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID", "")
DB_PATH = os.path.join(os.path.dirname(__file__), "data", "jobs.db")
