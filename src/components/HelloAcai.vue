<template>
  <b-card>
    <b-card-header>
      <b-card-title>Hello Açai</b-card-title>
    </b-card-header>
    <b-card-body>
      <b-form @submit="onSubmit" class="w-100">
        <div cols="4" class="container">
          <h1>{{ msg }}</h1>
          <b-row class="justify-content-center">
            <b-col cols="4" v-if="etapa === 0">
              <div>
                <b-row class="justify-content-center">
                  <h5 class="p-3">Selecione uma fruta para acompanhar</h5>
                  <b-form-select
                    v-model="addPedidoAcai.sabor"
                    :options="this.op_sabor"
                  ></b-form-select>
                  <h5 class="p-3">Escolha o Tamanho do seu Açai</h5>
                  <b-form-select
                    v-model="addPedidoAcai.tamanho"
                    :options="this.op_tam"
                  ></b-form-select> </b-row
                ><br />
                <b-button
                  @click="required"
                  class="mt-4"
                  pill
                  block
                  variant="outline-primary"
                  >Escolher Adicionais<b-icon icon="arrow-bar-right"></b-icon
                ></b-button>
              </div>
            </b-col>
            <b-col cols="4" v-else-if="etapa == 1">
              <div>
                <b-row class="justify-content-center">
                  <h5 class="p-3">Você deseja adicional?</h5>
                  <div>
                    <b-button
                      @click="adicional = true"
                      pill
                      variant="outline-success"
                      >Manda Ver<b-icon icon="arrow-bar-bottom"></b-icon
                    ></b-button>
                    <b-button
                      @click="
                        adicional = false;
                        addPedidoAcai.adicional = '';
                      "
                      pill
                      variant="outline-danger"
                      >Quero Não<b-icon icon="arrow-bar-right"></b-icon
                    ></b-button>
                    <span v-if="adicional === true" class="d-flex p-4">
                      <b-form-group label="Selecione um ou mais adicionais">
                        <b-form-radio-group
                          v-model="addPedidoAcai.adicional"
                          :options="op_adicional"
                          buttons
                          button-variant="outline-dark"
                        >
                        </b-form-radio-group>
                      </b-form-group>
                    </span>
                  </div> </b-row
                ><br />
                <b-button @click="etapa = 0" pill block variant="outline-danger"
                  >Calma, quero voltar<b-icon icon="arrow-bar-up"></b-icon
                ></b-button>
                <b-button
                  @click="addComanda"
                  class="mt-3"
                  pill
                  block
                  variant="outline-primary"
                  >Finalizar Pedido<b-icon icon="arrow-bar-right"></b-icon
                ></b-button>
              </div>
            </b-col>
            <b-col cols="4" v-else>
              <div style="width:90%;" class="p-3">
                <b-row class="justify-content-center">
                  <h5 class="p-3">Agora basta ver se está tudo certinho</h5>
                  <div>
                    <b-card no-body v-on="calcula()">
                      <b-table-simple>
                        <b-thead>
                          <b-th colspan="3">CONVERÊNCIA DE PEDIDO</b-th>
                        </b-thead>
                        <b-tbody>
                          <b-tr>
                            <b-td>Tamanho</b-td>
                            <b-td>
                              {{ addPedidoAcai.tamanho }} - R$
                              {{ valor_tamanho }},00</b-td
                            >
                          </b-tr>
                          <b-tr>
                            <b-td>Sabor</b-td>
                            <b-td> {{ addPedidoAcai.sabor }}</b-td>
                          </b-tr>
                          <b-tr>
                            <b-td>Adicional</b-td>
                            <b-td>
                              {{ addPedidoAcai.adicional }} - R$
                              {{ valor_adicional }},00</b-td
                            >
                          </b-tr>
                        </b-tbody>
                      </b-table-simple>
                      <b-card-text>
                        <p>Espera: {{ addPedidoAcai.tempo_preparo }} minutos</p>
                        <p>
                          Valor Total: R$ {{ addPedidoAcai.valor_total }},00
                        </p>
                      </b-card-text>
                    </b-card>
                  </div> </b-row
                ><br />
                <b-button
                  @click="
                    etapa = 0;
                    initForm();
                  "
                  pill
                  block
                  variant="outline-danger"
                  >Pera aí, vamos voltar<b-icon icon="arrow-bar-up"></b-icon
                ></b-button>
                <b-button type="submit" pill block variant="outline-primary"
                  >Tudo certo, pode pedir<b-icon
                    icon="arrow-bar-bottom"
                  ></b-icon
                ></b-button>
              </div>
            </b-col>
          </b-row>
        </div>
      </b-form>
    </b-card-body>
  </b-card>
</template>

<script>
import axios from "axios";

export default {
  name: "HelloWorld",
  data() {
    return {
      etapa: 0,
      adicional: false,
      msg: "Monte Seu Açaí",
      op_tam: [],
      op_sabor: [],
      valor_tamanho: 0,
      valor_adicional: 0,
      addPedidoAcai: {
        tamanho: "",
        sabor: "",
        adicional: "",
        tempo_preparo: 0,
        valor_total: 0
      }
    };
  },
  methods: {
    required() {
      if (this.addPedidoAcai.tamanho === undefined) {
        this.etapa = 0;
      } else if (this.addPedidoAcai.sabor === undefined) {
        this.etapa = 0;
      } else {
        this.etapa = 1;
      }
    },
    addComanda() {
      if (this.addPedidoAcai.adicional === undefined) {
        this.addPedidoAcai.adicional = "Sem adicional";
      }
      if (this.addPedidoAcai.tamanho === "Pequeno (300ml)") {
        this.valor_tamanho += 10;
      } else if (this.addPedidoAcai.tamanho === "Médio (500ml)") {
        this.valor_tamanho += 13;
      } else if (this.addPedidoAcai.tamanho === "Grande (700ml)") {
        this.valor_tamanho += 15;
      }
      if (this.addPedidoAcai.adicional === "Paçoca") {
        this.valor_adicional += 3;
      } else if (this.addPedidoAcai.adicional === "Leite Ninho") {
        this.valor_adicional += 3;
      }
      this.etapa = 2;
    },
    getData() {
      const path = "http://localhost:5000/pedido";
      axios
        .get(path)
        .then(res => {
          this.op_tam = res.data.dic_op.op_tam;
          this.op_sabor = res.data.dic_op.op_sabor;
          this.op_adicional = res.data.dic_op.op_adicional;
          this.addPedidoAcai.tamanho = res.data.tamanho;
          this.addPedidoAcai.sabor = res.data.sabor;
          this.addPedidoAcai.adicional = res.data.adicional;
          this.addPedidoAcai.tempo_preparo = res.data.tempo_preparo;
          this.addPedidoAcai.valor_total = res.data.valor_total;
        })
        .catch(error => {
          console.error(error);
        });
    },
    getPost(payload) {
      const path = "http://localhost:5000/pedido";
      axios
        .post(path, payload)
        .then(() => {
          this.getData();
        })
        .catch(error => {
          console.log(error);
          this.getData();
        });
    },
    initForm() {
      this.addPedidoAcai.tamanho = undefined;
      this.addPedidoAcai.sabor = undefined;
      (this.addPedidoAcai.adicional = []),
        (this.valor_tamanho = 0),
        (this.valor_adicional = 0);
    },
    onSubmit(e) {
      e.preventDefault();
      const payload = {
        tamanho: this.addPedidoAcai.tamanho,
        sabor: this.addPedidoAcai.sabor,
        adicional: this.addPedidoAcai.adicional
      };
      this.getPost(payload);
      this.initForm();
      this.etapa = 0;
    },
    calcula() {
      this.addPedidoAcai.tempo_preparo = 0;
      this.addPedidoAcai.valor_total = 0;
      if (this.addPedidoAcai.tamanho === "Pequeno (300ml)") {
        (this.addPedidoAcai.tempo_preparo += 5),
          (this.addPedidoAcai.valor_total += 10);
      }
      if (this.addPedidoAcai.tamanho === "Médio (500ml)") {
        (this.addPedidoAcai.tempo_preparo += 7),
          (this.addPedidoAcai.valor_total += 13);
      }
      if (this.addPedidoAcai.tamanho === "Grande (700ml)") {
        (this.addPedidoAcai.tempo_preparo += 10),
          (this.addPedidoAcai.valor_total += 15);
      }
      if (this.addPedidoAcai.sabor === "Kiwi") {
        this.addPedidoAcai.tempo_preparo += 5;
      }
      if (this.addPedidoAcai.adicional === "Paçoca") {
        (this.addPedidoAcai.tempo_preparo += 3),
          (this.addPedidoAcai.valor_total += 3);
      }
      if (this.addPedidoAcai.adicional == "Leite Ninho") {
        this.addPedidoAcai.valor_total += 3;
      }
      if (this.addPedidoAcai.adicional == []) {
        this.addPedidoAcai.adicional = "Sem Adicional";
      }
    }
  },
  created: function() {
    this.getData();
  }
};
</script>

<style scoped></style>
