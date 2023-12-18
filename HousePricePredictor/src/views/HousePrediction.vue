<template>
  <v-container>
    <v-row>
      <v-col cols="12" md="6">
        <v-card>
          <v-card-title class="bg-primary text-center border border-primary">
            Guide !!
          </v-card-title>
          <v-card-text>
            For accurate house price predictions,
            please provide the required information. Please fill in
            the following fields:
            <v-list>
              <v-list-item>
                <b>RM </b>: This field corresponds to the average number of rooms per dwelling
                in the neighbourhood.
              </v-list-item>
              <v-list-item>
                <b>LSTAT</b> : This field represents the percentage of the neighbourhood
                with a status below the average.
              </v-list-item>
              <v-list-item>
                <b>PTRATIO</b> : This field indicates the pupil/teacher ratio in the
                schools in the district.
              </v-list-item>
            </v-list>
          </v-card-text>
        </v-card>
      </v-col>
      <v-col cols="12" md="6">
        <v-card>
          <v-form @submit.prevent="submitForm" v-model="form" class="ma-5">
            <v-text-field
              v-model="formData.RM"
              :rules="[requiredRule, decimalRule]"
              label="RM"
              required
              variant="outlined"
            ></v-text-field>

            <v-text-field
              v-model="formData.LSTAT"
              :rules="[requiredRule, decimalRule]"
              label="LSTAT"
              required
              variant="outlined"
            ></v-text-field>

            <v-text-field
              v-model="formData.PTRATIO"
              :rules="[requiredRule, decimalRule]"
              label="PTRATIO"
              variant="outlined"
              required
            ></v-text-field>

            <v-btn type="submit" :loading="laoding" :disabled="!form" color="primary">GET PREDICTION</v-btn>
          </v-form>
        </v-card>
        <v-dialog v-model="showdialog" transition="dialog-bottom-transition"
        width="700">
            <v-card >
              <v-card-title class="text-end text-red" >
                <v-icon @click="showdialog=false">mdi-close</v-icon>
              </v-card-title>
                <v-card-text class="text-center">
                  A house with these features can be expensive: <b class="text-primary">{{ resultat.prediction.toFixed(2) }}</b>
            </v-card-text>
            </v-card>
        </v-dialog>
      </v-col>
    </v-row>
  </v-container>
</template>
  
  <script>
import { getAPI } from "../http/index.js";
export default {
  data() {
    return {
      formData: {
        RM: "",
        LSTAT: "",
        PTRATIO: "",
      },
      resultat:null,
      showdialog:false,
      form:false,
      loading:false,
      requiredRule: [(v) => !!v || "This field is required."],
      decimalRule: (v) =>
        /^\d+(\.\d+)?$/.test(v) || "Enter a valid decimal number.",
    };
  },
  methods: {
    submitForm() {
    this.loading=true;
        getAPI
          .post("/predict-house/", this.formData)
          .then((response) => {
            // Traiter la réponse
            this.resultat=response.data;
            this.showdialog=true;
            this.loading=false;
            this.formData.RM="";
            this.formData.LSTAT="";
            this.formData.PTRATIO="";

          })
          .catch((error) => {
            console.error(error);
            this.loading=false;

          });
    },
  },
};
</script>
<style  scoped>

.v-list{
    border-left: 4px solid #066aab;

}

</style>