"""Definição dos perfis Brasil e Internacional do JobRadar.

A lógica de execução fica em main.py; aqui ficam apenas regras, fontes,
cadência e termos de cada mercado.
"""

from dataclasses import dataclass, field

from config import (
    ATIVAR_EIXO_IBERICO_BR,
    CIDADES,
    CIDADES_EUROPA_IBERICA,
    FERRAMENTAS_TITULO,
    KEYWORDS,
    KEYWORDS_CARGO_AMBIGUO,
    KEYWORDS_CARGO_FORTE,
    KEYWORDS_EXCLUSAO_TITULO,
    MERCADOS_REMOTO_ACEITOS,
    PERMITIR_CARGO_AMBIGUO_SEM_QUALIFICADOR,
    QUALIFICADORES_CARGO,
    QUALIFICADORES_DADOS,
    TERMOS_BUSCA,
    TERMOS_CORE,
    TERMOS_POR_CICLO,
)
from config_intl import (
    ATIVAR_EIXO_IBERICO,
    CIDADES_INTL,
    DOMINIOS_INDEED_INTL,
    IDIOMAS_EXIGIDOS_INTL,
    KEYWORDS_INTL,
    LOCATIONS_INTL,
    MERCADOS_REMOTO_ACEITOS_INTL,
    TERMOS_BUSCA_INTL,
    TERMOS_POR_CICLO_INTL,
)
from job import RegrasFiltro
from scrapers.catho import CathoScraper
from scrapers.geekhunter import GeekHunterScraper
from scrapers.gupy import GupyScraper
from scrapers.indeed import IndeedScraper
from scrapers.indeed_intl import IndeedIntlScraper
from scrapers.jobs99 import Jobs99Scraper
from scrapers.linkedin import LinkedInScraper
from scrapers.linkedin_intl import LinkedInIntlScraper
from scrapers.solides import SolidesScraper
from scrapers.weworkremotely_intl import WeWorkRemotelyIntlScraper

FREQUENCIA_ALTA = "alta"
FREQUENCIA_BAIXA = "baixa"  # tenta somente na primeira execução do dia


@dataclass
class DefinicaoScraper:
    classe: type
    frequencia: str
    kwargs_extras: dict = field(default_factory=dict)


@dataclass
class Perfil:
    chave: str
    nome: str
    palavras_monitoradas: list[str]
    paises_pesquisados: list[str] | None
    regras: RegrasFiltro
    regras_eixo_secundario: RegrasFiltro | None
    eixo_secundario_ativo: bool
    eixo_secundario_rotulo: str
    termos_busca: list[str]
    termos_por_ciclo: int
    definicao_scrapers: list[DefinicaoScraper]
    termos_core: list[str] = field(default_factory=list)
    max_scrapers_concorrentes: int = 4


_REGRAS_BR = RegrasFiltro(
    keywords_forte=KEYWORDS_CARGO_FORTE,
    keywords_ambiguo=KEYWORDS_CARGO_AMBIGUO,
    qualificadores_dados=QUALIFICADORES_DADOS,
    ferramentas_titulo=FERRAMENTAS_TITULO,
    qualificadores_cargo=QUALIFICADORES_CARGO,
    cidades=CIDADES,
    mercados_remoto_aceitos=MERCADOS_REMOTO_ACEITOS,
    keywords_exclusao_titulo=KEYWORDS_EXCLUSAO_TITULO,
    permitir_ambiguo_sem_qualificador=PERMITIR_CARGO_AMBIGUO_SEM_QUALIFICADOR,
)

_REGRAS_BR_IBERIA = RegrasFiltro(
    keywords_forte=KEYWORDS_CARGO_FORTE,
    keywords_ambiguo=KEYWORDS_CARGO_AMBIGUO,
    qualificadores_dados=QUALIFICADORES_DADOS,
    ferramentas_titulo=FERRAMENTAS_TITULO,
    qualificadores_cargo=QUALIFICADORES_CARGO,
    cidades=CIDADES_EUROPA_IBERICA,
    keywords_exclusao_titulo=KEYWORDS_EXCLUSAO_TITULO,
    permitir_ambiguo_sem_qualificador=PERMITIR_CARGO_AMBIGUO_SEM_QUALIFICADOR,
)

# LinkedIn, Gupy e Sólides são as fontes de maior utilidade no perfil BR.
# Indeed tem retornado timeout/zero no runner do GitHub, então fica diário.
# Fontes de baixo rendimento permanecem como cobertura complementar 1x/dia.
_SCRAPERS_BR = [
    DefinicaoScraper(GupyScraper, FREQUENCIA_ALTA),
    DefinicaoScraper(LinkedInScraper, FREQUENCIA_ALTA),
    DefinicaoScraper(SolidesScraper, FREQUENCIA_ALTA),
    DefinicaoScraper(IndeedScraper, FREQUENCIA_BAIXA),
    DefinicaoScraper(CathoScraper, FREQUENCIA_BAIXA),
    DefinicaoScraper(GeekHunterScraper, FREQUENCIA_BAIXA),
    DefinicaoScraper(Jobs99Scraper, FREQUENCIA_BAIXA),
    DefinicaoScraper(WeWorkRemotelyIntlScraper, FREQUENCIA_BAIXA),
]

PERFIL_BR = Perfil(
    chave="brasil",
    nome="Brasil",
    palavras_monitoradas=KEYWORDS,
    paises_pesquisados=None,
    regras=_REGRAS_BR,
    regras_eixo_secundario=_REGRAS_BR_IBERIA,
    eixo_secundario_ativo=ATIVAR_EIXO_IBERICO_BR,
    eixo_secundario_rotulo="Ibéria",
    termos_busca=TERMOS_BUSCA,
    termos_por_ciclo=TERMOS_POR_CICLO,
    definicao_scrapers=_SCRAPERS_BR,
    termos_core=TERMOS_CORE,
    max_scrapers_concorrentes=4,
)


_REGRAS_INTL = RegrasFiltro(
    keywords_forte=KEYWORDS_INTL,
    keywords_ambiguo=[],
    qualificadores_dados=[],
    ferramentas_titulo=[],
    qualificadores_cargo=[],
    cidades=CIDADES_INTL,
    mercados_remoto_aceitos=MERCADOS_REMOTO_ACEITOS_INTL,
    idiomas_exigidos=IDIOMAS_EXIGIDOS_INTL,
)

_REGRAS_INTL_IBERIA = RegrasFiltro(
    keywords_forte=KEYWORDS_INTL,
    keywords_ambiguo=[],
    qualificadores_dados=[],
    ferramentas_titulo=[],
    qualificadores_cargo=[],
    cidades=CIDADES_EUROPA_IBERICA,
)

# LinkedIn Internacional continua a fonte primária. Indeed Intl e WWR foram
# medidos repetidamente como zero/anti-bot e passam a ser tentativa diária,
# reduzindo ~20-25 min de espera improdutiva em quase todos os ciclos.
_SCRAPERS_INTL = [
    DefinicaoScraper(LinkedInIntlScraper, FREQUENCIA_ALTA, {"locations": LOCATIONS_INTL}),
    DefinicaoScraper(IndeedIntlScraper, FREQUENCIA_BAIXA, {"dominios": DOMINIOS_INDEED_INTL}),
    DefinicaoScraper(WeWorkRemotelyIntlScraper, FREQUENCIA_BAIXA),
]

PERFIL_INTL = Perfil(
    chave="internacional",
    nome="Internacional",
    palavras_monitoradas=KEYWORDS_INTL,
    paises_pesquisados=LOCATIONS_INTL,
    regras=_REGRAS_INTL,
    regras_eixo_secundario=_REGRAS_INTL_IBERIA,
    eixo_secundario_ativo=ATIVAR_EIXO_IBERICO,
    eixo_secundario_rotulo="Ibéria",
    termos_busca=TERMOS_BUSCA_INTL,
    termos_por_ciclo=TERMOS_POR_CICLO_INTL,
    definicao_scrapers=_SCRAPERS_INTL,
    max_scrapers_concorrentes=3,
)

PERFIS = {
    PERFIL_BR.chave: PERFIL_BR,
    PERFIL_INTL.chave: PERFIL_INTL,
}
