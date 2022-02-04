<template>
  <ion-page>
    <div class="bg">
      <div class="container-fluid p-5 filter-this">
        <div class="text-center mt-4">
          <i class="fas fa-heartbeat fa-5x"></i>
        </div>
        <div>
          <h1 class="text-center fw-bold">
            Weight Loss <br />
            Tracker
          </h1>
        </div>

        <div class="container catchy-div ">
          <h1 class="text-center app-catchy">
            Transforming <br />
            Lifestyles
          </h1>
        </div>

        <div class='p-3 text-center register-div'>
            <ion-button shape="round" expand='block' router-direction='forward' router-link='/eaten'>Get Started</ion-button>
        </div>
        <div class="text-center text-dark">
          <p>Already have an account?</p>
          <ion-button fill='outline' color='dark' router-direction='forward' router-link='/eaten'>Signin</ion-button>

        </div>
      </div>
    </div>
  </ion-page>
</template>
<script>
import { IonPage, IonButton } from '@ionic/vue';

export default {
components : {
  IonPage, IonButton
}

};
</script>


<style>

.register-div {
  margin-top: 25vh;
}

.catchy-div {
  margin-top: 15vh;
}
.app-catchy {
  font-size: 40px;
  font-weight: 900;
}

.filter-this {
backdrop-filter: blur(100px);
width: 100%;
height: 100%;
}

.bg {
 background: rgb(237,87,107);
background: linear-gradient(216deg, rgba(237,87,107,1) 20%, rgba(1,85,126,1) 49%, rgba(237,87,107,1) 80%);
height: 100%;
}

</style>
