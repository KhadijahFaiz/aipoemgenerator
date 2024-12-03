<template>
  <div class="min-h-screen bg-gradient-to-r from-primary-100 via-secondary-100 to-primary-200 flex flex-col items-center justify-center p-4">
    <div class="bg-white bg-opacity-90 rounded-lg shadow-2xl p-8 max-w-xl w-full">
      <h1 class="text-4xl font-bold text-center text-gradient mb-6">
        Contact Us
      </h1>
      <p class="text-lg text-gray-700 mb-8 text-center">
        We'd love to hear from you! Whether you have a question, feedback, or just want to say hello, feel free to reach out.
      </p>

      <form @submit.prevent="submitForm" class="space-y-6">
        <div>
          <label for="name" class="block text-gray-700 text-sm font-bold mb-2">Your Name:</label>
          <input
            type="text"
            v-model="name"
            id="name"
            placeholder="Enter your name"
            class="input-primary"
            required
          />
        </div>
        <div>
          <label for="email" class="block text-gray-700 text-sm font-bold mb-2">Your Email:</label>
          <input
            type="email"
            v-model="email"
            id="email"
            placeholder="Enter your email"
            class="input-primary"
            required
          />
        </div>
        <div>
          <label for="message" class="block text-gray-700 text-sm font-bold mb-2">Your Message:</label>
          <textarea
            v-model="message"
            id="message"
            rows="4"
            placeholder="Type your message here..."
            class="input-primary"
            required
          ></textarea>
        </div>
        <button type="submit" class="btn-primary w-full">
          Send Message
        </button>
      </form>

      <div v-if="formSubmitted" class="mt-8 p-6 bg-gradient-to-br from-primary-100 to-secondary-100 rounded-lg shadow-inner-glow text-center">
        <h2 class="text-2xl font-semibold text-gray-800 mb-4">Thank You!</h2>
        <p class="text-gray-700">
          Your message has been sent. We'll get back to you soon.
        </p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'ContactView',
  data() {
    return {
      name: '',
      email: '',
      message: '',
      formSubmitted: false
    };
  },
  methods: {
    submitForm() {
      if (this.name && this.email && this.message) {
        // Simulate form submission
        this.formSubmitted = true;

        // Reset form fields
        this.name = '';
        this.email = '';
        this.message = '';
      } else {
        alert('Please fill in all fields before submitting.');
      }
    }
  }
};
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap');

* {
  font-family: 'Poppins', sans-serif;
}

.input-primary {
  width: 100%;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 4px;
  font-size: 16px;
  font-family: 'Poppins', sans-serif;
  outline: none;
  transition: border-color 0.3s ease;
}

.input-primary:focus {
  border-color: #42b983;
}

.btn-primary {
  background-color: #42b983;
  color: white;
  font-size: 18px;
  padding: 10px;
  border-radius: 4px;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.btn-primary:hover {
  background-color: #3a9d78;
}

.text-gradient {
  background: -webkit-linear-gradient(left, #42b983, #64c4a3);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}
</style>

  