<template>
  <v-container fluid>
    <v-row>
      <v-col class="d-flex justify-center mx-auto">
        <v-card max-width="800" class="mx-auto my-auto">
          <v-card-title class="bg-primary text-center border border-primary">
            Projects
          </v-card-title>
          <v-card-text>
            <v-card>
              <v-card-title class="h6"
                >Project 1: House price prediction(Machine
                Learning)</v-card-title
              >
              <v-card-text>
                This project aims to predict the price of a house based on the
                given features. The features include RM (average number of rooms
                per dwelling), LSTAT (percentage of homeowners with a lower
                socio-economic status), and PTRATIO (student-teacher ratio in
                the neighborhood schools). By utilizing these features, the
                model will be able to provide an estimation of the house price.
              </v-card-text>
            </v-card>
            <br />
            <v-card>
              <v-card-title class="h6"
                >Project 2: Feeling Analysis for film Reviews
                (NLP)</v-card-title
              >
              <v-card-text>
                This project analyses the sentiments of film reviews by asking
                users to enter a review for analysis. The project is able to
                automatically determine whether the review expresses a positive
                or negative sentiment.
              </v-card-text>
              
            </v-card>
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {};
</script>

<style>
</style>