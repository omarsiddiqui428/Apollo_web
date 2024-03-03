<template>
  <form @submit.prevent="submitForm">
    <img src="/Users/omarsiddiqui/Desktop/apollologo.png" class="logo">
    <label>Name:</label>
    <input type="text" required v-model="name">

    <label>Email:</label>
    <input type="email" required v-model="email">

    <label>Username:</label>
    <input type="text" required v-model="username">

    <label>Genre:</label>
    <select v-model="genre">
      <option value="pop"> Pop </option>
      <option value="rock"> Rock </option>
      <option value="hip hop"> Hip Hop </option>
      <option value="r&b"> R&B </option>
      <option value="country"> Country </option>
      <option value="electronic"> Electronic </option>
      <option value="jazz"> Jazz </option>
      <option value="classical"> Classical </option>
    </select>

    <label>Years of experience in the music industry:</label>
    <select v-model="years_experience">
      <option value="0"> less than 1 </option>
      <option value="1"> 1 </option>
      <option value="2"> 2 </option>
      <option value="3"> 3 </option>
      <option value="4"> 4 </option>
      <option value="5"> 5 </option>
      <option value="6"> 6 </option>
      <option value="7"> 7 </option>
      <option value="8"> 8 </option>
      <option value="9"> 9 </option>
      <option value="10"> 10 </option>
      <option value="10+"> more than 10 </option>
    </select>

    <label>Number of tracks on streaming services:</label>
    <select v-model="num_tracks">
      <option value="0"> none </option>
      <option value="1"> 1 </option>
      <option value="2"> 2 </option>
      <option value="3"> 3 </option>
      <option value="4"> 4 </option>
      <option value="5"> 5 </option>
      <option value="6"> 6 </option>
      <option value="7"> 7 </option>
      <option value="8"> 8 </option>
      <option value="9"> 9 </option>
      <option value="10"> 10 </option>
      <option value="11"> 11 </option>
      <option value="12"> 12 </option>
      <option value="13"> 13 </option>
      <option value="14"> 14 </option>
      <option value="15"> 15 </option>
      <option value="16"> 16 </option>
      <option value="17"> 17 </option>
      <option value="18"> 18 </option>
      <option value="19"> 19 </option>
      <option value="20"> 20 </option>
      <option value="20+"> more than 20 </option>
    </select>

    <label>Maximum streams on a single track:</label>
    <select v-model="max_streams">
      <option value="0-1k"> 0-1,000 </option>
      <option value="1k-5k"> 1,000-5,000 </option>
      <option value="5k-10k"> 5,000-10,000 </option>
      <option value="10k-20k"> 10,000-20,000 </option>
      <option value="20k-50k"> 20,000-50,000 </option>
      <option value="50k-100k"> 50,000-100,000 </option>
      <option value="100k-300k"> 100,000-300,000 </option>
      <option value="300k-500k"> 300,000-500,000 </option>
      <option value="500k-700k"> 500,000-700,000 </option>
      <option value="700k-1m"> 700,000-1M </option>
      <option value="1m-2m"> 1M-2M </option>
      <option value="2m-5m"> 2M-5M </option>
      <option value="5m-10m"> 5M-10M </option>
      <option value="10m-15m"> 10M-15M </option>
      <option value="15m-20m"> 15M-20M </option>
      <option value="20m+"> 20M+ </option>
    </select>

    <label>What support would you like a mentor to be able to provide?</label>
    <div class="checkbox-container">
      <div>
        <input type="checkbox" value="social_media_marketing" v-model="support_desired">
        <label>Social media marketing</label>
      </div>
      <div>
        <input type="checkbox" value="print_marketing" v-model="support_desired">
        <label>Print marketing</label>
      </div>
      <div>
        <input type="checkbox" value="general_industry_knowledge" v-model="support_desired">
        <label>General industry knowledge</label>
      </div>
      <div>
        <input type="checkbox" value="branding" v-model="support_desired">
        <label>Branding</label>
      </div>
      <div>
        <input type="checkbox" value="sound_development" v-model="support_desired">
        <label>Sound development</label>
      </div>
      <div>
        <input type="checkbox" value="production" v-model="support_desired">
        <label>Production</label>
      </div>
      <div>
        <input type="checkbox" value="live_show_logistics" v-model="support_desired">
        <label>Live show logistics</label>
      </div>
      <div>
        <input type="checkbox" value="listener_engagement" v-model="support_desired">
        <label>Listener engagement</label>
      </div>
      <div>
        <input type="checkbox" value="streaming_logistics" v-model="support_desired">
        <label>Streaming logistics</label>
      </div>
      <div>
        <input type="checkbox" value="booking_assistance" v-model="support_desired">
        <label>Booking assistance</label>
      </div>

    </div>

    <label>Please select the revenue models you would be open to below:</label>
    <div class="checkbox-container">
      <div>
        <input type="checkbox" value="pro_bono" v-model="rev_model">
        <label>Pro-bono</label>
      </div>
      <div>
        <input type="checkbox" value="fee_per" v-model="rev_model">
        <label>Fee per session</label>
      </div>
      <div>
        <input type="checkbox" value="rev_sharing" v-model="rev_model">
        <label>Revenue sharing</label>
      </div>
    </div>

    <div class="terms">
      <input type="checkbox" v-model="terms"required>
      <label>Accept terms and conditions (Required) </label>
    </div>

    <button type="submit">Submit</button>

  </form>
  <p>Name: {{name}}</p>
  <p>Email: {{email}}</p>
  <p>Username: {{username}}</p>
  <p>Genre: {{genre}}</p>
  <p>Years of experience in music: {{years_experience}}</p>
  <p>Number of tracks on streaming services: {{num_tracks}}</p>
  <p>Max single track streams: {{max_streams}}</p>
  <p>Support/guidance desired: {{support_desired}}</p>
  <p>Revenue models interested in: {{rev_model}} </p>
  <p>Terms accepted: {{terms}}</p>





</template>

<script>
import axios from 'axios';

export default{ //with two way data binding, why do we want it to be bound from the data to the input?
  data() {
    return{
      name: '',
      email: '',
      username: '',
      genre: '',
      years_experience:'',
      num_tracks: '',
      max_streams: '',
      support_desired:[],
      rev_model:[],
      terms: false,

    }
  },
  methods: {

    async submitForm() {
      try{ // Grouping the data
        const formData = {
          name: this.name,
          email: this.email,
          username: this.username,
          genre: this.genre,
          years_of_experience: this.years_experience,
          num_tracks_streaming: this.num_tracks,
          max_streams: this.max_streams,
          support_desired: this.support_desired,
          revenue_model: this.rev_model,
          terms: this.terms,
        };
        // POST request
        const response = await axios.post('/api/submit-form',formData);

        //response
        console.log(response.data);
      }
      catch(error){

        console.error('Error submitting form:', error)
      }
    },
  },

}
</script>

<style>
.logo {
  float: left;
  max-width: 350px;
  margin-bottom: 30px;
}
form{
  max-width: 420px;
  margin: 30px auto;
  background: palegreen;
  text-align: left;
  padding: 40px;
  border-radius: 10px;
}
label {
  color: black;
  display: inline-block;
  margin: 25px 0 15px;
  font-size: 0.6em;
  text-transforming: uppercase;
  letter-spacing: 1px;
  font-weight: bold;
}
input, select {
  display: block;
  padding: 10px 6px;
  width: 100%;
  box-sizing: border-box;
  border: none;
  border-bottom: 1px solid #ddd;
  color: black;
}
input[type = "checkbox"] {
  display: inline-block;
  width: 16px;
  margins: 0 10px 0 0;
  position: relative;
  top: 2px;
}
.checkbox-container {
  display: grid;
  justify-content: space-between;
}
</style>
