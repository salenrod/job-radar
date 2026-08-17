import os
from dotenv import load_dotenv

load_dotenv()

# -----------------------------------------------------------------------------
# PERFIL BRASIL - CLOUD SECURITY / DETECTION ENGINEERING / SECURITY OPERATIONS
# -----------------------------------------------------------------------------
#
# IMPORTANTE:
# Alguns nomes de variaveis (ex.: QUALIFICADORES_DADOS) foram mantidos porque
# fazem parte da interface esperada pelo job.py do projeto original. O conteudo,
# no entanto, foi totalmente adaptado para Cybersecurity.


# Cargos fortes: titulos suficientemente especificos para Cloud Security,
# Detection Engineering, SOC/SecOps, SIEM, Threat Hunting e Incident Response.
# Basta o titulo conter um deles para o filtro de cargo considerar a vaga.
KEYWORDS_CARGO_FORTE = [
    # Cloud Security
    "Cloud Security Engineer",
    "Cloud Security Analyst",

    # Detection Engineering / Threat Detection
    "Detection Engineer",
    "Security Detection Engineer",
    "Threat Detection Engineer",
    "Detection and Response Engineer",

    # SOC / SecOps
    "SOC Analyst",
    "Analista SOC",
    "Analista de SOC",
    "Security Operations Analyst",
    "Security Operations Engineer",
    "SecOps Engineer",

    # SIEM / Security Monitoring
    "SIEM Engineer",
    "SIEM Analyst",
    "Engenheiro SIEM",
    "Analista SIEM",

    # Threat Hunting / Incident Response / Blue Team
    "Threat Hunter",
    "Threat Hunting Analyst",
    "Incident Response Engineer",
    "Incident Response Analyst",
    "Blue Team Engineer",
    "Blue Team Analyst",
]


# Cargos ambiguos: existem em varias subareas de seguranca. Para evitar vagas
# de GRC, compliance, awareness, AppSec puro, IAM puro ou vulnerabilidades, eles
# so passam se o TITULO tambem contiver um qualificador tecnico da lista abaixo.
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
    "Engenheiro de Seguranca",
    "Especialista em Seguranca",
    "Especialista em Seguranca da Informacao",
]


# O nome da variavel e legado do projeto original e precisa ser preservado.
# Na pratica, estes sao QUALIFICADORES_DE_SEGURANCA. Um cargo ambiguo acima
# precisa conter pelo menos um destes termos no titulo para ser aprovado.
QUALIFICADORES_DADOS = [
    # Cloud
    "cloud",
    "nuvem",
    "aws",
    "azure",
    "gcp",

    # Detection / SOC / SIEM
    "detection",
    "detecao",
    "soc",
    "secops",
    "security operations",
    "siem",
    "splunk",
    "sentinel",
    "qradar",
    "security monitoring",
    "monitoramento",

    # Endpoint / response / hunting
    "edr",
    "xdr",
    "defender",
    "crowdstrike",
    "threat",
    "ameaca",
    "hunting",
    "incident response",
    "resposta a incidentes",
    "dfir",
    "soar",

    # Detection-as-Code / analytics
    "kql",
    "spl",
    "sigma",
    "mitre",
]


# Ferramentas/plataformas que podem aparecer como o nucleo do titulo, por
# exemplo "Splunk Engineer" ou "Microsoft Sentinel Analyst". O projeto so
# aprova esse caminho quando tambem ha uma palavra de cargo no titulo.
FERRAMENTAS_TITULO = [
    "Splunk",
    "Microsoft Sentinel",
    "Sentinel",
    "QRadar",
    "SIEM",
    "Defender XDR",
    "Microsoft Defender",
    "CrowdStrike",
    "EDR",
    "XDR",
]


# Palavras de cargo aceitas quando o titulo e centrado numa ferramenta.
QUALIFICADORES_CARGO = [
    "analista",
    "analyst",
    "engenheiro",
    "engineer",
    "especialista",
    "specialist",
    "arquiteto",
    "architect",
    "consultor",
    "consultant",
    "hunter",
]


KEYWORDS = KEYWORDS_CARGO_FORTE + KEYWORDS_CARGO_AMBIGUO


# -----------------------------------------------------------------------------
# TERMOS DE BUSCA
# -----------------------------------------------------------------------------
# KEYWORDS define o que pode passar no filtro de titulo.
# TERMOS_BUSCA define o que os scrapers efetivamente pesquisam.
#
# TERMOS_CARGO e derivado automaticamente das keywords para que todo cargo
# aceito pelo filtro tambem tenha chance de ser pesquisado.
TERMOS_CARGO_EXTRA = [
    "cloud security",
    "detection engineering",
    "threat detection",
    "security operations",
    "soc cybersecurity",
    "siem security",
    "threat hunting",
]

TERMOS_CARGO = sorted(
    set(k.lower() for k in KEYWORDS) | set(TERMOS_CARGO_EXTRA)
)


# Termos de stack com alto valor para o perfil alvo. Evitei uma lista enorme
# porque cada termo adicional aumenta o custo/tempo das rodadas de scraping.
TERMOS_FERRAMENTA = [
    "splunk security",
    "microsoft sentinel",
    "defender xdr",
    "qradar siem",
    "aws security",
    "azure security",
]

TERMOS_BUSCA = TERMOS_CARGO + TERMOS_FERRAMENTA


# O projeto usa rodizio de termos para controlar o custo de cada execucao.
# 12 oferece cobertura um pouco mais rapida que o default 10 sem transformar
# cada ciclo em uma busca gigantesca.
TERMOS_POR_CICLO = 12


# -----------------------------------------------------------------------------
# LOCALIZACAO - BRASIL
# -----------------------------------------------------------------------------
# A lista e uma whitelist. "Remoto" fica primeiro por ser a modalidade mais
# importante; as demais cidades cobrem os principais polos de tecnologia do BR.
# Se quiser somente remoto, basta deixar CIDADES = ["Remoto"].
CIDADES = [
    "Remoto",
    "São Paulo",
    "Campinas",
    "Barueri",
    "Rio de Janeiro",
    "Belo Horizonte",
    "Curitiba",
    "Florianópolis",
    "Porto Alegre",
    "Brasília",
    "Recife",
]


# Lista compartilhada com config_intl.py. Mantida para compatibilidade com o
# projeto original. O eixo presencial/hibrido iberico permanece desligado.
CIDADES_EUROPA_IBERICA = [
    "Portugal",
    "Lisboa",
    "Porto",
    "Braga",
    "Espanha",
    "España",
    "Spain",
    "Madrid",
    "Barcelona",
    "Valencia",
]

ATIVAR_EIXO_IBERICO_BR = False


# Mercado principal do pipeline BR. Aqui o LinkedIn pode retornar presencial,
# hibrido e remoto; o filtro de CIDADES acima decide o que realmente passa.
LOCATIONS_LINKEDIN = ["Brasil"]


# Mercados externos pesquisados apenas com filtro remoto no LinkedIn. Mantive
# LATAM + Iberia, que sao coerentes com a arquitetura atual do projeto e evitam
# inundar o radar com vagas "US only" de mercados onde work authorization tende
# a ser um bloqueio frequente.
LOCATIONS_LINKEDIN_REMOTO_APENAS = [
    "Argentina",
    "Chile",
    "México",
    "Colômbia",
    "Espanha",
    "Portugal",
]


# Quando uma vaga remota declara explicitamente um mercado, ele precisa bater
# nesta allowlist. Vagas realmente worldwide/anywhere sao tratadas pelo job.py
# como sem restricao explicita e nao dependem desta lista.
MERCADOS_REMOTO_ACEITOS = [
    "Brasil",
    "LATAM",
    "Argentina",
    "Chile",
    "México",
    "Colômbia",
    "Portugal",
    "Espanha",
]


# -----------------------------------------------------------------------------
# EXECUCAO / DIGEST / TELEGRAM
# -----------------------------------------------------------------------------
INTERVALO_MINUTOS = int(os.getenv("INTERVALO_MINUTOS", 180))


# Com a configuracao de Cybersecurity, score 6 ja representa um sinal forte
# interessante (ex.: cargo forte + mercado + senioridade neutra). Assim vagas
# bem alinhadas podem chegar imediatamente e o restante fica no digest.
LIMIAR_DIGEST_IMEDIATO = 6


# 0 UTC = 21:00 no horario de Brasilia (UTC-3).
DIGEST_HORA_UTC = 0


TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID", "")


DB_PATH = os.path.join(os.path.dirname(__file__), "data", "jobs.db")
