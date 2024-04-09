<script>
  import "../app.css";
  import { afterNavigate, beforeNavigate } from "$app/navigation";

  let isLoading = false;

  beforeNavigate(() => {
    isLoading = true;
  });

  afterNavigate(() => {
    isLoading = false;
  });
</script>

<div class="min-h-screen flex flex-col">
  <header class="bg-blue-500 text-white p-4">
    <h2>Zdravíčko</h2>
  </header>

  <main class="flex-1 p-4 m-auto">
    <slot />
  </main>
</div>

{#if isLoading}
  <div
    class="fixed inset-0 bg-gray-600 bg-opacity-50 flex items-center justify-center z-50"
  >
    <div class="loader" />
  </div>
{/if}

<style>
  .loader {
    border: 4px solid #f3f3f3;
    border-top: 4px solid #3498db;
    border-radius: 50%;
    width: 40px;
    height: 40px;
    animation: spin 2s linear infinite;
  }

  @keyframes spin {
    0% {
      transform: rotate(0deg);
    }
    100% {
      transform: rotate(360deg);
    }
  }
</style>
