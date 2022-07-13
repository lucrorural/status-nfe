from datetime import datetime

import requests
from bs4 import BeautifulSoup


class DisponibilidadeNFe(object):

    def __init__(self):
        self.__URL = 'https://www.nfe.fazenda.gov.br/portal/disponibilidade.aspx'

        self.headers = {
            'Connection': 'keep-alive',
            'Cache-Control': 'max-age=0',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36',  # noqa
            'DNT': '1',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',    # noqa
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7,mt;q=0.6,gl;q=0.5,he;q=0.4,ru;q=0.3,pl;q=0.2,la;q=0.1,es;q=0.1,fr;q=0.1,de;q=0.1,cy;q=0.1,und;q=0.1'  # noqa
        }

    def _request(self):
        try:
            data = requests.get(
                self.__URL,
                headers=self.headers,
                timeout=None
            )
        except Exception as error:
            raise error
        return data

    def get_status(self):
        request = self._request()
        html = request.content

        sefaz_data = []
        # Fazer o parse do HTML
        try:
            soup = BeautifulSoup(html, 'html.parser')
            table = soup.find(id="ctl00_ContentPlaceHolder1_gdvDisponibilidade2")

            for tr in table.find_all("tr"):
                # Eliminar o cabeçalho
                if tr.th is not None:
                    continue

                # Fazer parse do TD
                info = []
                for td in tr.find_all("td"):
                    if td.img is not None:
                        info.append(td.img["src"].split("_")[1])
                        continue

                    info.append(td.get_text())

                autorizador = info[0]
                autorizacao = info[1]
                retorno_autorizacao = info[2]
                inutilizacao = info[3]
                consulta_protocolo = info[4]
                status_servico = info[5]
                tempo_medio = info[6]
                consulta_cadastro = info[7]
                recepcao_evento = info[8]
                ultima_verificacao = table.caption.span.get_text().split(" - ")[1].split(": ")[1]

                # “13/07/2022 16:17:21” -> YYYY-MM-DD HH:MM[:ss[.uuuuuu]][TZ].']
                ultima_verificacao_format = datetime.strptime(ultima_verificacao, "%d/%m/%Y %H:%M:%S")

                sefaz_data.append(
                    {
                        'autorizador': autorizador,
                        'autorizacao': autorizacao,
                        'retorno_autorizacao': retorno_autorizacao,
                        'inutilizacao': inutilizacao,
                        'consulta_protocolo': consulta_protocolo,
                        'status_servico': status_servico,
                        'tempo_medio': tempo_medio,
                        'consulta_cadastro': consulta_cadastro,
                        'recepcao_evento': recepcao_evento,
                        'ultima_verificacao': ultima_verificacao_format
                    }
                )
            return sefaz_data

        except BaseException as err:
            return err
