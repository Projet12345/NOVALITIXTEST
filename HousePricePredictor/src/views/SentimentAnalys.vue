<template>
  <v-container>
    <v-row>
      <v-col class="d-flex justify-center mx-auto">
        <v-card min-width="500"  class="mx-auto my-auto">
          <v-card-title class="bg-primary text-center border border-primary">
            Guide !!
          </v-card-title>
          <v-card-text>
            <p>We'd love to hear what you think about our movies!</p>
            <p>Please take a moment to share your experience with us.</p>
            <v-form @submit.prevent="submitReview" v-model="form">
              <v-textarea
                :rules="requiredRule"
                v-model="review"
                label="Your review"
              ></v-textarea>
              <v-btn type="submit" :disabled="!form" color="primary" :loading="loading"
                >Send MY REVIEW</v-btn
              >
            </v-form>
          </v-card-text>
        </v-card>
      </v-col>
      <v-dialog
        v-model="showdialog"
        transition="dialog-bottom-transition"
        width="700"
      >
        <v-card>
          <v-card-title
            v-if="result != null && result >= 0.5"
            class="d-flex justify-space-between bg-primary"
          >
            <h4>Positive review</h4>
            <v-icon @click="showdialog = false">mdi-close</v-icon>
          </v-card-title>

          <v-card-text
            v-if="result != null && result >= 0.5"
            class="text-center"
          >
            We're very pleased to hear that you like our movies. Thank you for
            your <Strong class="text-green">Positive</Strong>review. <br />
            <v-icon class="text-primary">mdi-emoticon-happy</v-icon>
          </v-card-text>

          <v-card-title
            v-if="result != null && result < 0.5"
            class="d-flex justify-space-between bg-red"
          >
            <h4>Negative review</h4>
            <v-icon @click="showdialog = false">mdi-close</v-icon>
          </v-card-title>
          <v-card-text
            v-if="result != null && result < 0.5"
            class="text-center"
          >
            We're very sorry to hear that you didn't like our movies. <br />
            <v-icon class="text-red">mdi-emoticon-sad</v-icon> <br />
            We will make every effort to improve them.
          </v-card-text>
        </v-card>
      </v-dialog>
    </v-row>
  </v-container>
</template>

<script>
import { getAPI } from "../http/index.js";
export default {
  data() {
    return {
      review: "",
      result: null,
      requiredRule: [(v) => !!v || "This field is required."],
      form: false,
      showdialog: false,
      loading:false
    };
  },
  methods: {
    submitReview() {
      this.loading=true
      getAPI
        .post("/predict-review/", { new_review: this.review })
        .then((response) => {
          // Traiter la réponse
          this.result = response.data.prediction[0][0];
          this.showdialog = true;
          this.review="";
          this.loading=false
        })
        .catch((error) => {
          console.error(error);
          this.showdialog = true;
          this.loading=false
        });
    },
  },
};
</script>

<style>
</style>