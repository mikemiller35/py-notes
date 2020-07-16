<template>
  <div class="container">
    <div class="row">
      <div class="col-sm-10">
        <h1>Notes</h1>
        <hr/>
        <br/><br/>
        <button type="button" class="btn btn-success btn-sm" v-b-modal.note-modal>Add Note</button>
        <br/><br/>
        <table class="table table-hover">
          <thead>
            <tr>
              <th scope="col">ID</th>
              <th scope="col">Note</th>
              <th></th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(note, index) in notes" :key="index">
              <td>{{ note.id }}</td>
              <td>{{ note.body }}</td>
              <td>
                <div class="btn-group" role="group">
                  <!-- <button type="button" class="btn btn-danger btn-sm">Delete</button> -->
                </div>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
    <b-modal ref="addNoteModal"
    id="note-modal"
    title="Add a new note"
    hide-footer>
    <b-form @submit="onSubmit" @reset="onReset" class="w-100">
      <b-form-group id="form-body-group"
      label="Note:"
      label-for="form-note-input">
      <b-form-input id="form-note-input"
      type="text"
      v-model="addNoteForm.body"
      required
      placeholder="Enter note">
    </b-form-input>
  </b-form-group>
  <b-button-group>
    <b-button type="submit" variant="primary">Submit</b-button>
    <b-button type="reset" variant="danger">Reset</b-button>
  </b-button-group>
</b-form>
</b-modal>
</div>
</template>

<script>
  import axios from "axios";
  
  export default {
    data() {
      return {
        notes: [],
        addNoteForm: {
        body: '',
      },
      };
    },
    methods: {
      getNotes() {
        const path = "http://localhost:5000/api/notes";
        axios
        .get(path)
        .then(res => {
          this.notes = res.data.notes;
        })
        .catch(error => {
          // eslint-disable-next-line
          console.error(error);
        });
      },
      addNote(payload) {
        const path = 'http://localhost:5000/api/notes';
        axios.post(path, payload)
        .then(() => {
          this.getNotes();
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.log(error);
          this.getNotes();
        });
      },
      initForm() {
        this.addNoteForm.body = '';
      },
      onSubmit(evt) {
        evt.preventDefault();
        this.$refs.addNoteModal.hide();
        const payload = {
          body: this.addNoteForm.body
        };
        this.addNote(payload);
        this.initForm();
      },
      onReset(evt) {
        evt.preventDefault();
        this.$refs.addNoteModal.hide();
        this.initForm();
      },
    },
    created() {
      this.getNotes();
    },
  };
</script>
