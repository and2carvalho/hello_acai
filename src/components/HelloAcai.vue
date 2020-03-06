<template>
  <b-card>
    <b-card-header>
      <b-card-title>Hello Açai</b-card-title>
    </b-card-header>
    <b-card-body>
      <div class="container">
        <h1>{{ msg }}</h1>
        <b-row>
          <b-col>
            <div>
              <b-row class="justify-content-center">
                <h5 class="p-3">Escolha o Tamanho do seu Açai</h5>
                <b-form-select :options="op_tam" required="true"></b-form-select>
                <h5 class="p-3">Selecione uma fruta para acompanhar</h5>
                <b-form-select :options="op_fruta" required="true"></b-form-select>
              </b-row><br>
              <b-button class="mt-4" pill block>Escolher Adicionais<b-icon icon="arrow-bar-right"></b-icon></b-button>
            </div>
          </b-col>
          <b-col>
            <div>
              <b-row class="justify-content-center">
                <h5 class="p-3">Você deseja adicional?</h5>
                <div>
                  <b-button pill>Manda Ver<b-icon icon="arrow-bar-bottom"></b-icon></b-button>
                  <b-button pill>Quero Não<b-icon icon="arrow-bar-right"></b-icon></b-button>
                  <span class="d-flex p-4">
                    <b-form-group label="Selecione um ou mais adicionais">
                      <b-form-checkbox-group
                        v-model="selected"
                        :options="op_adicional"
                        buttons
                      >
                        </b-form-checkbox-group>
                    </b-form-group>
                  </span>
                </div>
              </b-row><br>
              <b-button class="mt-3" pill block>Finalizar Pedido<b-icon icon="arrow-bar-right"></b-icon></b-button>
            </div>
          </b-col>
          <b-col>
            <div style="width:65%;" class="border p-3">
              <b-row class="justify-content-center">
                <h5 class="p-3">Agora basta ver se está tudo certinho</h5>
                <div>
                  <b-card no-body>
                    <b-table-simple>
                      <b-thead>
                        <b-th colspan="3">Pedido Número: {{ pedido.num }}</b-th>
                      </b-thead>
                      <b-tbody>
                        <b-tr>
                          <b-td>Tamanho</b-td>
                          <b-td> {{ pedido.tamanho }} </b-td>
                        </b-tr>
                        <b-tr>
                          <b-td>Sabor</b-td>
                          <b-td> {{ pedido.sabor }} </b-td>
                        </b-tr>
                        <b-tr v-for="item in pedido.adicional" :key="item">
                          <b-td>Adicional</b-td>
                          <b-td> {{ item }} </b-td>
                        </b-tr>
                      </b-tbody>
                    </b-table-simple>
                    <b-card-text> 
                      <p>Tempo de Preparo: {{  pedido.tempo_preparo }}</p>
                      <p>Valor Total: {{  pedido.valor_total }}</p>
                    </b-card-text>
                  </b-card>
                </div>
              </b-row><br>
              <b-button class="mt-3" pill block>Tudo certo, pode pedir<b-icon icon="arrow-bar-up"></b-icon></b-button>
            </div>
          </b-col>
        </b-row>
      </div>
    </b-card-body>
  </b-card>
</template>

<script>
export default {
  name: "HelloWorld",
  data() {
    return {
      msg: "Monte Seu Açaí",
      op_tam: ["Pequeno (300ml)", "Médio(500ml)", "Grande(700ml)"],
      op_fruta: ["Morango", "Banana", "Kiwi"],
      op_adicional: ["Granola", "Paçoca", "Leite Ninho"],
      adicional_escolha: [],
      pedido: {
        num: "12524",
        tamanho: "Médio",
        sabor: "Morango",
        adicional: ["Granola","Leite Ninho"],
        tempo_preparo: "20 min",
        valor_total: "R$ 23,00"
      }
    }
  }
};
</script>


<style scoped>
</style>
