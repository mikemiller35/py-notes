<template>
	<div class="container">
		<div class="row">
			<div class="col-sm-10">
				<h1>Notes</h1>
				<hr />
				<br /><br />
				<button type="button" class="btn btn-success btn-sm">Add Note</button>
				<br /><br />
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
									<button type="button" class="btn btn-danger btn-sm">Delete</button>
								</div>
							</td>
						</tr>
					</tbody>
				</table>
			</div>
		</div>
	</div>
</template>

<script>
import axios from "axios";

export default {
	data() {
		return {
			notes: []
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
		}
	},
	created() {
		this.getNotes();
	}
};
</script>
