from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/submit-form', methods=['POST'])
def submit_form():
    try:
        form_data = request.json
        #Data is in the form below
        # formData = {
        #     name: this.name,
        #     email: this.email,
        #     username: this.username,
        #     genre: this.genre,
        #     years_of_experience: this.years_experience,
        #     num_tracks_streaming: this.num_tracks,
        #     max_streams: this.max_streams,
        #     support_desired: this.support_desired,
        #     revenue_model: this.rev_model,
        #     terms: this.terms,}

        with open('userdata.json', 'r') as file:
            user_data= json.load(file)
            if form_data[username] not in user_data:
                user_data[(form_data[username])] = {
                    "name": form_data[name],
                    "email": form_data[email],
                    "genre": form_data[genre],
                    "years_of_experience": form_data[years_of_experience],
                    "num_tracks_streaming": form_data[num_tracks_streaming],
                    "max_streams": form_data[max_streams],
                    "support_desired": form_data[support_desired],
                    "revenue_model": form_data[revenue_model],
                    "terms":form_data[terms]
                    }
                with open('userdata.json', 'w') as file:
                    json.dump(user_data, file, indent=4)
                return 'Form submitted successfully'
            else:
                return 'Error 400: Username already in use. Please choose a different one'

    except Exception as e:
        return jsonify({'error': str(e)}), 500 #what is this??

if __name__=='__main__':
    app.run(debug=True)
