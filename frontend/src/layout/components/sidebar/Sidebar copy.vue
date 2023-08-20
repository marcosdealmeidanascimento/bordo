<template>
  <aside>
    <nav></nav>
  </aside>
</template>

<script>
export default {};
</script>

<style>
aside {
  transform: translateX(0px);
  background-image: url(https://demos.creative-tim.com/vue-material-dashboard/img/sidebar-2.32103624.jpg) !important;
  background-size: cover !important;
  position: absolute;
  top: 0;
  bottom: 0;
  background: #fff;
  z-index: 1000;
}
@media (min-width: 1000px) {
  aside {
    width: 250px;
  }
}
nav {
  height: 100%;
  width: 100%;
  background-color: rgba(1, 1, 1, 0.75);
}
</style>
