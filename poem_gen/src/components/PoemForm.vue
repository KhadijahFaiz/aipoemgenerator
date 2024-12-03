<template>
  <form @submit.prevent="onSubmit" class="poem-form">
    <div class="form-group">
      <label for="theme">Theme:</label>
      <select v-model="theme" id="theme" required>
        <option value="">Select a theme</option>
        <option value="Nature">Nature</option>
        <option value="Love">Love</option>
        <option value="Loss">Loss</option>
        <option value="Identity">Identity</option>
      </select>
    </div>
    <div class="form-group">
      <label for="style">Style:</label>
      <select v-model="style" id="style">
        <option value="">Select a style (optional)</option>
        <option value="Sonnet">Sonnet</option>
        <option value="Free Verse">Free Verse</option>
        <option value="Haiku">Haiku</option>
      </select>
    </div>
    <div class="form-group">
      <label for="emotion">Emotion:</label>
      <select v-model="emotion" id="emotion">
        <option value="">Select an emotion (optional)</option>
        <option value="Joy">Joy</option>
        <option value="Sadness">Sadness</option>
        <option value="Anger">Anger</option>
        <option value="Fear">Fear</option>
      </select>
    </div>
    <button type="submit">Generate Poem</button>
  </form>
</template>

<script>
import { ref, onMounted, watch } from 'vue'

export default {
  name: 'PoemForm',
  emits: ['generate'],
  setup(props, { emit }) {
    const theme = ref('')
    const style = ref('')
    const emotion = ref('')

    // Load form data from localStorage when the component mounts
    onMounted(() => {
      const savedFormData = localStorage.getItem('poemFormData')
      if (savedFormData) {
        const { theme: savedTheme, style: savedStyle, emotion: savedEmotion } = JSON.parse(savedFormData)
        theme.value = savedTheme || ''
        style.value = savedStyle || ''
        emotion.value = savedEmotion || ''
      }
    })

    // Watch for changes in theme, style, and emotion, and store them in localStorage
    watch([theme, style, emotion], () => {
      const formData = { theme: theme.value, style: style.value, emotion: emotion.value }
      localStorage.setItem('poemFormData', JSON.stringify(formData))
    })

    const onSubmit = () => {
      if (!theme.value) {
        alert('Please select a theme.')
        return
      }
      emit('generate', { theme: theme.value, style: style.value, emotion: emotion.value })
    }

    return {
      theme,
      style,
      emotion,
      onSubmit
    }
  }
}
</script>

<style scoped>
.poem-form {
  max-width: 400px;
  margin: 0 auto;
  padding: 1rem;
  background-color: #f9f9f9;
  border-radius: 8px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

.form-group {
  margin-bottom: 15px;
}

label {
  display: block;
  margin-bottom: 5px;
}

select {
  width: 100%;
  padding: 8px;
  border: 1px solid #ddd;
  border-radius: 4px;
}

button {
  background-color: #42b983;
  color: white;
  padding: 10px 15px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

button:hover {
  background-color: #3aa876;
}
</style>
