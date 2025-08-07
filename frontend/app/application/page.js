// app/application/page.js
export default function ApplicationForm() {
  return (
    <div className="max-w-xl mx-auto bg-white p-8 shadow rounded-lg">
      <h2 className="text-2xl font-bold mb-6 text-green-900">Application Form</h2>
      <form className="space-y-4">
        <div>
          <label>Full Names</label>
          <input type="text" name="fullName" />
        </div>
        <div>
          <label>Email</label>
          <input type="email" name="email" />
        </div>
        <div>
          <label>Phone</label>
          <input type="text" name="phone" />
        </div>
        <div>
          <label>Upload File</label>
          <input type="file" />
        </div>
        <button type="submit">Submit</button>
      </form>
    </div>
  );
}
