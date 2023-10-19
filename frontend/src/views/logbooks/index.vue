<template>
    <router-link to="/home">Voltar</router-link>
    <form @submit.prevent="createLogbook">
        <div class="flex">
            <div class="mr-5">
                <p>Name</p>
                <InputText v-model="name" required placeholder="Name" />
            </div>
            <div>
                <p>Description</p>
                <InputText v-model="description" placeholder="Description" />
            </div>
        </div>
        <Button label="Create Logbook" type="submit" class="mt-5" />
    </form>
    <DataTable :value="logbooks" paginator :first="0" :rows="10" :loading="loading" v-model:editingRows="editingRows"
        editMode="row" dataKey="id" @row-edit-save="onRowEditSave" stripedRows removableSort>
        <Column sortable field="name" header="Name">
            <template #editor="{ data, field }">
                <InputText v-model="data[field]" />
            </template>
        </Column>
        <Column field="description" header="Description">
            <template #editor="{ data, field }">
                <InputText v-model="data[field]" />
            </template>
        </Column>
        <Column sortable field="user_id" header="User ID" />
        <Column :rowEditor="true" style="width: 10%; min-width: 8rem" bodyStyle="text-align:center" />
        <Column style="width: 10%; min-width: 8rem" bodyStyle="text-align:center">
            <template #body="{ data }">
                <Button icon="pi pi-trash" class="p-button-rounded p-button-danger" @click="removeLogbook(data)" />
            </template>
        </Column>
    </DataTable>
    <div class="grid">
        <div class="col-6 p-3" v-for="logbook in logbooks">
            <Logbook :logbook="logbook" />
        </div>
    </div>
    <Toast />
    <ConfirmDialog />
</template>

<script setup>
import { ref, onMounted } from "vue";
import apiClient from '@/helpers/axios'
import Logbook from "./components/Logbook.vue";

const flex = ref("display: flex;")

import { useConfirm } from "primevue/useconfirm";
const confirm = useConfirm();


import Toast from 'primevue/toast';
import { useToast } from 'primevue/usetoast';
const toast = useToast();

const loading = ref(false);

const name = ref("");
const description = ref("");
const user_id = ref("");

const editingRows = ref([]);
const logbooks = ref([]);

const getLogbooks = async () => {
    loading.value = true;
    try {
        const response = await apiClient.get("logbook");
        logbooks.value = response.data;
        loading.value = false;
    } catch {
        toast.add({
            severity: 'error',
            summary: 'Error',
            detail: 'Logbooks not found',
            life: 3000
        });
    }
}

const createLogbook = async () => {
    try {
        const response = await apiClient.post("logbook", {
            name: name.value,
            description: description.value,
            user_id: user_id.value,
        });
        if (response.error) {
            toast.add({
                severity: 'error',
                summary: 'Error',
                detail: 'Logbook not created',
                life: 3000
            });
        } else {
            toast.add({
                severity: 'success',
                summary: 'Success',
                detail: 'Logbook created',
                life: 3000
            });
        }
        getLogbooks();
    } catch (err) {
        toast.add({
            severity: 'error',
            summary: 'Error',
            detail: 'Logbook not created',
            life: 3000
        });

    }

}

const onRowEditSave = async (event) => {
    let { newData, index } = event;
    logbooks.value[index] = newData;
    await apiClient.put("logbook/" + newData.id, {
        name: newData.name,
        description: newData.description,
        user_id: newData.user_id,
    });

    getLogbooks();

}

const removeLogbook = async (event) => {
    let data = event;
    confirm.require({
        message: 'Do you want to delete this record?',
        header: 'Delete Confirmation',
        icon: 'pi pi-info-circle',
        acceptClass: 'p-button-danger',
        accept: async () => {
            await apiClient.delete("logbook/" + data.id);
            getLogbooks();
            toast.add({ severity: 'info', summary: 'Confirmed', detail: 'Logbook deleted', life: 3000 });
        },
        reject: () => {
            getLogbooks();
            toast.add({ severity: 'error', summary: 'Rejected', detail: 'Logbook not deleted', life: 3000 });
        }
    });
}

onMounted(() => {
    const user = JSON.parse(localStorage.getItem("user"))
    user_id.value = user.id
    getLogbooks();
})

</script>
