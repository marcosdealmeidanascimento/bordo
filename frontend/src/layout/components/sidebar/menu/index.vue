<template>
  <PanelMenu :model="items"  v-model:expandedKeys="expandedKeys">
    <template class="mb-2" #item="{item}">
        <a
         :href="item.url">
         <i :class=item.icon></i
            ><span
              class="link"
            >{{item.label}}</span
          ></a>
    </template>
</PanelMenu>

</template>
<script setup>
import { ref } from 'vue';
import PanelMenu from 'primevue/panelmenu';
        const expandedKeys = ref({});
        const items = ref([
            {
                key: '0',
                label: 'File',
                icon: 'pi pi-fw pi-file',
                items: [{
                        key: '0_0',
                        label: 'New',
                        icon: 'pi pi-fw pi-plus',                       
                    },
                    {
                        key: '0_1',
                        label: 'Delete',
                        icon: 'pi pi-fw pi-trash'
                    },
                    {
                        key: '0_2',
                        label: 'Export',
                        icon: 'pi pi-fw pi-external-link'
                    }
                ]
            },
            {
                key: '1',
                label: 'user',
                icon: 'pi pi-fw pi-pencil',
                items: [{
                        key: '1_0',
                        label: 'Left',
                        icon: 'pi pi-fw pi-align-left'
                    },
                    {
                        key: '1_1',
                        label: 'Right',
                        icon: 'pi pi-fw pi-align-right'
                    },
                    {
                        key: '1_2',
                        label: 'Center',
                        icon: 'pi pi-fw pi-align-center'
                    },
                    {
                        key: '1_3',
                        label: 'Justify',
                        icon: 'pi pi-fw pi-align-justify'
                    }
                ]
            },{
                key: '2',
                label: 'user',
                icon: 'pi pi-fw pi-pencil',
                items: [{
                        key: '2_0',
                        label: 'Left',
                        icon: 'pi pi-fw pi-align-left'
                    },
                    {
                        key: '2_1',
                        label: 'Right',
                        icon: 'pi pi-fw pi-align-right'
                    },
                    {
                        key: '3_2',
                        label: 'Center',
                        icon: 'pi pi-fw pi-align-center'
                    },
                    {
                        key: '3_3',
                        label: 'Justify',
                        icon: 'pi pi-fw pi-align-justify'
                    }
                ]
            },
        ]);

        const expandAll = () => {
            for (let node of nodes.value) {
                expandNode(node);
            }

            expandedKeys.value = {...expandedKeys.value};
        };
        const collapseAll = () => {
            expandedKeys.value = {};
        };
        const expandNode = (node) => {
            if (node.children && node.children.length) {
                expandedKeys.value[node.key] = true;

                for (let child of node.children) {
                    expandNode(child);
                }
            }
        };

</script>

<style lang="css">
.p-panelmenu .p-panelmenu-panel {
   margin-bottom: 5px !important; 
}
.p-panelmenu .p-panelmenu-header .p-panelmenu-header-content {
    padding: 0.5rem !important;
    transition-duration: 150ms !important;
    border: none !important; 
    background-color: var(--indigo-700) !important;
    color: var(--indigo-100) !important;
    align-items: center !important;
    display: flex !important;
    flex-direction: column;
    cursor: pointer;
    margin: 5px;
}
.p-panelmenu-content{
    margin: 5px;
}
.p-menuitem-content{
    padding-left: 10px;
    cursor: pointer;
    margin-bottom: 5px;
}
</style>