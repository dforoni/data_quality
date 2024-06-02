import pandera as pa
from pandera import Field, Check

class DataModel(pa.SchemaModel):

    """
    Modelo de dados para contratos, usando pandas e pandera para validação de esquema.

    Attributes:
        data_assinatura_contrato (pa.typing.Series[str]): Data de assinatura do contrato. Não pode ser nulo.
        data_publicacao_dou (pa.typing.Series[str]): Data de publicação no Diário Oficial da União. Não pode ser nulo.
        data_inicio_vigencia (pa.typing.Series[str]): Data de início de vigência do contrato. Não pode ser nulo.
        data_fim_vigencia (pa.typing.Series[str]): Data de fim de vigência do contrato. Não pode ser nulo.
        orgao_superior_contratante (pa.typing.Series[str]): Órgão superior contratante. Não pode ser nulo.
        orgao_entidade_vinculada_contratante (pa.typing.Series[str]): Órgão ou entidade vinculada contratante. Não pode ser nulo.
        unidade_gestora_contratante (pa.typing.Series[str]): Unidade gestora contratante. Não pode ser nulo.
        forma_de_contratacao (pa.typing.Series[str]): Forma de contratação. Não pode ser nulo.
        grupo_de_objeto_de_contratacao (pa.typing.Series[str]): Grupo de objeto de contratação. Não pode ser nulo.
        numero_do_contrato (pa.typing.Series[str]): Número do contrato. Não pode ser nulo.
        nome_do_fornecedor (pa.typing.Series[str]): Nome do fornecedor. Pode ser nulo.
        cpf_cnpj_do_fornecedor (pa.typing.Series[str]): CPF ou CNPJ do fornecedor. Não pode ser nulo e deve ser único.
        situacao (pa.typing.Series[str]): Situação do contrato. Não pode ser nulo.
        valor_contratado (pa.typing.Series[str]): Valor contratado. Não pode ser nulo.
    """

    data_assinatura_contrato: pa.typing.Series[str] = Field(nullable=False)
    data_publicacao_dou: pa.typing.Series[str] = Field(nullable=False)
    data_inicio_vigencia: pa.typing.Series[str] = Field(nullable=False)
    data_fim_vigencia: pa.typing.Series[str] = Field(nullable=False)
    orgao_superior_contratante: pa.typing.Series[str] = Field(nullable=False)
    orgao_entidade_vinculada_contratante: pa.typing.Series[str] = Field(nullable=False)
    unidade_gestora_contratante: pa.typing.Series[str] = Field(nullable=False)
    forma_de_contratacao: pa.typing.Series[str] = Field(nullable=False)
    grupo_de_objeto_de_contratacao: pa.typing.Series[str] = Field(nullable=False)
    numero_do_contrato: pa.typing.Series[str] = Field(nullable=False)
    nome_do_fornecedor: pa.typing.Series[str] = Field(nullable=True)
    cpf_cnpj_do_fornecedor: pa.typing.Series[str] = Field(nullable=False, unique=True)
    situacao: pa.typing.Series[str] = Field(nullable=False)
    valor_contratado: pa.typing.Series[str] = Field(nullable=False)

    @pa.dataframe_check
    def check_index(cls, df: pa.typing.DataFrame) -> bool:
        index = df.index
        return index.min() >= 0 and index.max() <= 8633

    class Config:
        coerce = True
        strict = True # fica restrito apenas para as colunas especificadas acima