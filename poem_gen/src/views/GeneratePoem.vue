<template>
  <div class="min-h-screen bg-gradient-to-r from-gray-200 to-gray-300 flex flex-col items-center justify-center p-4">
    <div class="bg-white bg-opacity-90 rounded-lg shadow-2xl p-8 flex flex-row w-full max-w-screen-xl">
      <PoemForm @generate="generatePoem" :initialFormData="savedFormData" class="flex-shrink-0 w-1/3 p-4" />
        
      <div class="flex-grow w-2/3 p-4">
        <div v-if="generatedPoem">
          <PoemDisplay :poem="generatedPoem" class="max-w-full" />

          <div v-if="poemImage" class="image-container mt-4">
            <h2 class="text-2xl font-semibold">Generated Poem Image:</h2>
            <img :src="poemImage" alt="Generated Poem" class="mt-2 border rounded poem-image" />
            <a :href="poemImage" download="poem_image.png" class="bg-blue-500 text-white py-2 px-4 rounded hover:bg-blue-700 mt-4 inline-block">Save Poem Image</a>
          </div>
        </div>

        <div class="mt-4">
          <button
            @click="savePoem"
            class="bg-indigo-500 hover:bg-indigo-700 text-white font-bold py-2 px-4 rounded"
          >
            Save Poem Text
          </button>
          <button
            @click="speakPoem(generatedPoem)"
            class="bg-green-500 hover:bg-green-700 text-white font-bold py-2 px-4 rounded ml-2"
          >
            Read Poem Aloud
          </button>
          <button
            @click="pausePoem"
            class="bg-yellow-500 hover:bg-yellow-700 text-white font-bold py-2 px-4 rounded ml-2"
          >
            Pause
          </button>
          <button
            @click="resumePoem"
            class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded ml-2"
          >
            Resume
          </button>
          <button
            @click="stopPoem"
            class="bg-red-500 hover:bg-red-700 text-white font-bold py-2 px-4 rounded ml-2"
          >
            Stop
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { ref, onMounted } from 'vue'
import axios from 'axios'
import PoemForm from '@/components/PoemForm.vue'
import PoemDisplay from '@/components/PoemDisplay.vue'

export default {
  name: 'GeneratePoem',
  components: { PoemForm, PoemDisplay },
  setup() {
    const generatedPoem = ref('')
    const poemImage = ref('') // To store the generated poem image
    const speech = ref(null)
    const savedFormData = ref(null) // For storing restored form data

    const generatePoem = async (formData) => {
      try {
        const response = await axios.post('http://127.0.0.1:5001/api/generate-poem', formData)
        generatedPoem.value = response.data.poem
        poemImage.value = response.data.image // Store the generated image data
        localStorage.setItem('generatedPoem', response.data.poem) // Save poem to localStorage
        localStorage.setItem('poemImage', response.data.image) // Save image to localStorage
        localStorage.setItem('poemFormData', JSON.stringify(formData)) // Save form data
      } catch (error) {
        console.error('Error generating poem:', error)
      }
    }

    // Load the saved poem and form data from localStorage when the component mounts
    onMounted(() => {
      const savedPoem = localStorage.getItem('generatedPoem')
      if (savedPoem) {
        generatedPoem.value = savedPoem
      }

      const savedImage = localStorage.getItem('poemImage')
      if (savedImage) {
        poemImage.value = savedImage // Restore the image from localStorage
      }

      const savedFormDataStr = localStorage.getItem('poemFormData')
      if (savedFormDataStr) {
        savedFormData.value = JSON.parse(savedFormDataStr) // Restore form data
      }
    })

    const savePoem = () => {
      if (generatedPoem.value) {
        const savedPoems = JSON.parse(localStorage.getItem('savedPoems') || '[]')
        savedPoems.push(generatedPoem.value)
        localStorage.setItem('savedPoems', JSON.stringify(savedPoems))
        alert('Poem text saved successfully!')
      }
    }

    const speakPoem = (poem) => {
      if (speech.value) {
        window.speechSynthesis.cancel()
      }
      speech.value = new SpeechSynthesisUtterance(poem)
      speech.value.lang = 'en-US'
      speech.value.pitch = 1
      speech.value.rate = 1
      window.speechSynthesis.speak(speech.value)
    }

    const pausePoem = () => {
      if (window.speechSynthesis.speaking && !window.speechSynthesis.paused) {
        window.speechSynthesis.pause()
      }
    }

    const resumePoem = () => {
      if (window.speechSynthesis.paused) {
        window.speechSynthesis.resume()
      }
    }

    const stopPoem = () => {
      if (window.speechSynthesis.speaking) {
        window.speechSynthesis.cancel()
        speech.value = null
      }
    }

    return {
      generatedPoem,
      poemImage, // Make poemImage available in the template
      generatePoem,
      savePoem,
      speakPoem,
      pausePoem,
      resumePoem,
      stopPoem,
      savedFormData // Make savedFormData available in the template
    }
  }
}
</script>

<style scoped>
.poem-display {
  background-color: #ecf0f1;
  border-radius: 8px;
  padding: 1.5rem;
  margin-top: 2rem;
  max-width: 100%;
  word-wrap: break-word;
}

.poem-display h2 {
  font-size: 1.5rem;
  color: #2c3e50;
  margin-bottom: 1rem;
}

.poem-display pre {
  white-space: pre-wrap; /* Ensures long lines wrap */
  font-family: 'Georgia', serif;
  font-style: italic;
  color: #34495e;
  line-height: 1.6;
  margin: 0;
}

.image-container {
  background-color: #f7f9fa; /* Light gray background for the image container */
  padding: 16px; /* Padding for the container */
  border-radius: 8px; /* Rounded corners */
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1); /* Subtle shadow for depth */
}

img.poem-image {
  width: 100%; /* Set to 100% to fill the container */
  height: auto; /* Keep aspect ratio */
  max-height: 400px; /* Maximum height for the image */
  border: 2px solid #3498db;
  border-radius: 8px;
}
</style>
