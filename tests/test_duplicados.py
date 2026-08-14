from organizador.duplicados import calcular_hash, encontrar_duplicados


def test_arquivos_com_mesmo_conteudo_tem_mesmo_hash(tmp_path, criar_arquivo):
    a = criar_arquivo(tmp_path / "a.txt", "mesmo conteudo")
    b = criar_arquivo(tmp_path / "b.txt", "mesmo conteudo")
    assert calcular_hash(a) == calcular_hash(b)


def test_arquivos_com_conteudo_diferente_tem_hash_diferente(tmp_path, criar_arquivo):
    a = criar_arquivo(tmp_path / "a.txt", "conteudo 1")
    b = criar_arquivo(tmp_path / "b.txt", "conteudo 2")
    assert calcular_hash(a) != calcular_hash(b)


def test_encontrar_duplicados_agrupa_apenas_repetidos(tmp_path, criar_arquivo):
    a = criar_arquivo(tmp_path / "a.txt", "repetido")
    b = criar_arquivo(tmp_path / "b.txt", "repetido")
    c = criar_arquivo(tmp_path / "c.txt", "unico")

    duplicados = encontrar_duplicados([a, b, c])

    assert len(duplicados) == 1
    grupo = next(iter(duplicados.values()))
    assert set(grupo) == {a, b}


def test_sem_duplicados_retorna_dicionario_vazio(tmp_path, criar_arquivo):
    a = criar_arquivo(tmp_path / "a.txt", "1")
    b = criar_arquivo(tmp_path / "b.txt", "2")

    assert encontrar_duplicados([a, b]) == {}
