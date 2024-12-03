<template>
  <div class="poem-display">
    <h3>Generated Poem</h3>
    <pre>{{ poem }}</pre>
   
  </div>
</template>

<script>
export default {
  name: 'PoemDisplay',
  props: {
    poem: {
      type: String,
      required: true
    }
  },
  setup(props) {
    const savePoem = () => {
      // Implement logic to save the poem (e.g., to local storage or backend)
      console.log('Saving poem:', props.poem)
      // Example implementation:
      localStorage.setItem('savedPoem', props.poem)
    }

    return {
      savePoem
    }
  }
}
</script>

<style scoped>
.poem-display {
  margin-top: 20px;
  padding: 20px;
  border: 1px solid #ddd;
  border-radius: 4px;
}

pre {
  white-space: pre-wrap;
  word-wrap: break-word;
  text-align: left;
  font-family: 'Courier New', Courier, monospace;
}

button {
  margin-top: 10px;
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
