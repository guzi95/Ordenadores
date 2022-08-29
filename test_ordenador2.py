import ordenador
import pytest
import conta_tempos

class TestaOrdenador:

    @pytest.fixture
    def o(self):
        return ordenador.Ordenador()

    @pytest.fixture
    def l_aleatoria(self):
        c = conta_tempos.ContaTempos()
        return c.lista_aleatoria(100)

    @pytest.fixture
    def l_quase(self):
        c = conta_tempos.ContaTempos()
        return c.lista_quase_ordenada(100)

    def esta_ordenada(self, l):
        for i in range(len(l) - 1):
            if l[i] > l[i + 1]:
                return False
        return True

    def test_bolha_curta_aleat(self, o, l_aleatoria):
        o.bolha_curta(l_aleatoria)
        assert self.esta_ordenada(l_aleatoria)

    def test_selecao_direta_aleat(self, o, l_aleatoria):
        o.selecao_direta(l_aleatoria)
        assert self.esta_ordenada(l_aleatoria)

    def test_bolha_curta_quase(self, o, l_quase):
        o.bolha_curta(l_quase)
        assert self.esta_ordenada(l_quase)

    def test_selecao_direta_quase(self, o, l_quase):
        o.selecao_direta(l_quase)
        assert self.esta_ordenada(l_quase)

