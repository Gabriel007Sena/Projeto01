import requests 

def obter_cidades_por_estado():
    ufs_brasil = [
        "AC",  # Acre
        "AL",  # Alagoas
        "AP",  # Amapá
        "AM",  # Amazonas
        "BA",  # Bahia
        "CE",  # Ceará
        "DF",  # Distrito Federal
        "ES",  # Espírito Santo
        "GO",  # Goiás
        "MA",  # Maranhão
        "MT",  # Mato Grosso
        "MS",  # Mato Grosso do Sul
        "MG",  # Minas Gerais
        "PA",  # Pará
        "PB",  # Paraíba
        "PR",  # Paraná
        "PE",  # Pernambuco
        "PI",  # Piauí
        "RJ",  # Rio de Janeiro
        "RN",  # Rio Grande do Norte
        "RS",  # Rio Grande do Sul
        "RO",  # Rondônia
        "RR",  # Roraima
        "SC",  # Santa Catarina
        "SP",  # São Paulo
        "SE",  # Sergipe
        "TO"   # Tocantins
    ]
    cidades_por_estado = {}
    for uf in ufs_brasil:
        response = requests.get(f'https://servicodados.ibge.gov.br/api/v1/localidades/estados/{uf}/distritos')
        lista_cidades = [municipio["nome"] for municipio in response.json()]
        cidades_por_estado[uf] = lista_cidades
    return cidades_por_estado

def obter_todas_cidades():
    url = f'https://servicodados.ibge.gov.br/api/v1/localidades/distritos'
    response = requests.get(url)
    lista_cidades = [cidade["municipio"]["nome"] for cidade in response.json()]
    return lista_cidades

if __name__ == "__main__":
    cidades_por_estado = obter_cidades_por_estado()
    print(cidades_por_estado)
