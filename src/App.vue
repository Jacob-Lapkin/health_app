<template>
  <ion-app>
    <ion-router-outlet />
  </ion-app>
</template>

<script>
import { IonApp, IonRouterOutlet } from '@ionic/vue';
import { defineComponent } from 'vue';

export default defineComponent({
  name: 'App',
  components: {
    IonApp,
    IonRouterOutlet
  }
});
</script>


<style>


.primary-font {
  font-family: 'Montserrat Alternates', sans-serif !important;
}
 ion-label, ion-content, ion-header, ion-card, ion-button, ion-title {
     font-family: 'Montserrat Alternates', sans-serif !important;
 }
 h1, h2, h3, h4, h5 {
     font-family: 'Montserrat Alternates', sans-serif !important;
 }

 .primary-color {
   color: #ff4961 !important;
 }

</style>