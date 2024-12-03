<template>
  <nav class="navbar">
    <div class="nav-container">
      <div class="nav-links">
        <router-link to="/" class="nav-link" exact>Home</router-link>
        <router-link to="/about" class="nav-link">About</router-link>
        <router-link to="/contact" class="nav-link">Contact Us</router-link>
        <router-link to="/generate" class="nav-link">Generate Poem</router-link>
        <router-link to="/gallery" class="nav-link">Poem Gallery</router-link>
      </div>
    </div>
  </nav>
</template>

<script lang="ts">
export default {
  name: 'NavBar'
}
</script>

<style scoped lang="scss">
.navbar {
  background: linear-gradient(to right, #2c3e50, #3498db);
  padding: 0.5rem 2rem;
  position: sticky;
  top: 0;
  z-index: 1000;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);

  .nav-container {
    max-width: 1200px;
    margin: 0 auto;
  }

  .nav-links {
    display: flex;
    justify-content: center;
    align-items: center;
  }

  .nav-link {
    font-weight: 600;
    color: #ecf0f1;
    text-decoration: none;
    padding: 0.75rem 1.25rem;
    margin: 0 0.25rem;
    border-radius: 25px;
    transition: all 0.3s ease;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    font-size: 0.9rem;

    &:hover {
      background-color: rgba(255, 255, 255, 0.2);
      transform: translateY(-2px);
    }

    &.router-link-exact-active {
      color: #2c3e50;
      background-color: #ecf0f1;
      box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2);
    }
  }
}

@media (max-width: 768px) {
  .navbar {
    padding: 0.5rem 1rem;

    .nav-links {
      flex-wrap: wrap;
      justify-content: flex-start;
    }

    .nav-link {
      padding: 0.5rem 0.75rem;
      margin: 0.25rem;
      font-size: 0.8rem;
    }
  }
}

@media (max-width: 480px) {
  .navbar {
    .nav-links {
      flex-direction: column;
      align-items: flex-start;
    }

    .nav-link {
      width: 100%;
      text-align: left;
      padding: 0.75rem;
      border-radius: 0;
      margin: 0;
      border-bottom: 1px solid rgba(255, 255, 255, 0.1);

      &:last-child {
        border-bottom: none;
      }
    }
  }
}
</style>