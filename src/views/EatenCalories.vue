<template>
  <ion-page>
    <ion-header>
      <ion-toolbar class="pt-5">
      <ion-title color='primary'>Eaten</ion-title>

      <ion-buttons slot="start">
        <ion-back-button>back</ion-back-button>
      </ion-buttons>
    </ion-toolbar>
    </ion-header>
    <ion-content :fullscreen="true">
      <div class="p-3">
          <h1>Total Calories:</h1><h4 class='primary-color'>1,422,1044</h4>
      </div>
      <div class="border-bottom mb-3">
          <ion-row>
            <ion-col><p class="ms-3">Steak</p></ion-col>
            <ion-col><p>+200</p></ion-col>
            <ion-col>Feb-12-2021</ion-col>
          </ion-row>
      </div>
      <div class="border-bottom mb-3">
          <ion-row>
            <ion-col><p class="ms-3">Steak</p></ion-col>
            <ion-col><p>+200</p></ion-col>
            <ion-col>Feb-12-2021</ion-col>
          </ion-row>
      </div>
      <div class="border-bottom mb-3">
          <ion-row>
            <ion-col><p class="ms-3">Steak</p></ion-col>
            <ion-col><p>+200</p></ion-col>
            <ion-col>Feb-12-2021</ion-col>
          </ion-row>
      </div>
      
    </ion-content>
  </ion-page>
</template>

<script>
import { IonPage, IonHeader, IonTitle, IonContent, IonRow, IonCol, IonBackButton, IonButtons, IonToolbar } from '@ionic/vue';

export default  {
  components: { IonHeader, IonTitle, IonContent, IonPage, IonRow, IonCol, IonBackButton, IonButtons, IonToolbar  }
}
</script>