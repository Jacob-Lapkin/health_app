<template>
  <ion-page>
    <ion-header>
      <ion-toolbar class="pt-5">
        <ion-title class="primary-font" color='primary'>Home</ion-title>
      </ion-toolbar>
    </ion-header>
    <ion-content :fullscreen="true">
      <div class="container-fluid ps-4 pt-4">
      <ion-card-title>Hello Jacob</ion-card-title>
        <h4>Weekly Summary</h4>
      </div>

<!-- card for calories counted -->
      <ion-card>
    <ion-card-header>
      <h2 class="primary-font">Calories Eaten</h2>
      <ion-card-title>23,000</ion-card-title>
    </ion-card-header>

    <ion-card-content>
       <ion-list>
    <ion-item>
      <ion-label>Poké bowl</ion-label><div><ion-label color='primary'>+ 800</ion-label></div>
    </ion-item>
    <ion-item>
      <ion-label>Steak</ion-label><div><ion-label color='primary'>+ 400</ion-label></div>
    </ion-item>
    <ion-item>
      <ion-label>Fiber one bar</ion-label><div><ion-label color='primary'>+ 100</ion-label></div>
    </ion-item>
    <ion-item>
      <ion-label>Pepsi</ion-label><div><ion-label color='primary'>+ 150</ion-label></div>
    </ion-item>
  </ion-list>
      <div class="mt-3">
  <ion-button expand="block" fill="outline" router-direction='forward' router-link='/eaten'> View Calories</ion-button>

      </div>
    </ion-card-content>
  </ion-card>

  <!-- calories for workout -->
   <ion-card>
    <ion-card-header>
      <h2 class="primary-font">Calories Burned</h2>
      <ion-card-title>3,000</ion-card-title>
    </ion-card-header>

    <ion-card-content>
       <ion-list>
    <ion-item>
      <ion-label class="text-start">Tennis</ion-label><ion-label class="text-center">2 Hours</ion-label><ion-label color='primary' class="text-end">- 800</ion-label>
    </ion-item>
    <ion-item>
      <ion-label class="text-start">Run</ion-label><ion-label class="text-center">0.5 Hours</ion-label><ion-label color='primary' class="text-end">- 200</ion-label>
    </ion-item>
    <ion-item>
      <ion-label class="text-start">Surf</ion-label><ion-label class="text-center">1 Hours</ion-label><ion-label color='primary' class="text-end">- 1000</ion-label>
    </ion-item>
    <ion-item>
      <ion-label class="text-start">Gym</ion-label><ion-label class="text-center">2 Hours</ion-label><ion-label color='primary' class="text-end">- 1400</ion-label>
    </ion-item>
  </ion-list>
      <div class="mt-3">
  <ion-button expand="block" fill="outline" router-direction='forward' router-link='/eaten'> View Calories</ion-button>

      </div>
    </ion-card-content>
  </ion-card>
    
    </ion-content>
  </ion-page>
</template>

<script>
import { IonPage, IonHeader, IonToolbar, IonTitle, IonContent, IonCard,
 IonCardContent, IonCardHeader, IonCardTitle, IonButton, IonList, IonItem, IonLabel} from '@ionic/vue';

export default  {
  components: { IonHeader, IonToolbar, IonTitle, IonContent, IonPage,
   IonCard, IonCardContent,  IonCardHeader, IonCardTitle, IonButton, IonList, IonItem, IonLabel},
}

</script>