import React, { Component } from 'react'
import axios from 'axios'

class Form extends Component {
	constructor(props) {
		super(props)
		this.state = {
			work_year: undefined,
			experience_level: undefined,
			employment_type: undefined,
			job_title: undefined,
			employee_residence: undefined,
			remote_ratio: undefined,
			company_location: undefined,
			company_size: undefined,
			salary: undefined
		}
		this.handleChange = this.handleChange.bind(this)
		this.handleSubmit = this.handleSubmit.bind(this)
	}

	handleSubmit(event) {
		const { work_year,
			experience_level,
			employment_type,
			job_title,
			employee_residence,
			remote_ratio,
			company_location,
			company_size
		} = this.state
		event.preventDefault()
		alert(`Sending Data : \n
			work_year : ${work_year}
			experience_level : ${experience_level}
			employment_type : ${employment_type}
			job_title : ${job_title}
			employee_residence : ${employee_residence}
			remote_ratio: ${remote_ratio}
			company_location: ${company_location}
			company_size: ${company_size}
			`)

		axios({
			url: 'http://127.0.0.1:5000/predict',
			method: 'POST',
			data: {
				work_year: work_year,
				experience_level: experience_level,
				employment_type: employment_type,
				job_title: job_title,
				employee_residence: employee_residence,
				remote_ratio: remote_ratio,
				company_location: company_location,
				company_size: company_size
			},
			headers: { "Content-Type": 'application/json' }
		}).then((res) => {
			console.log(res.data)
			this.setState({
				work_year: work_year,
				experience_level: experience_level,
				employment_type: employment_type,
				job_title: job_title,
				employee_residence: employee_residence,
				remote_ratio: remote_ratio,
				company_location: company_location,
				company_size: company_size,
				salary: res.data.salary
			});
		})
	}

	handleChange(event) {
		this.setState({
			[event.target.name]: event.target.value
		})
	}

	gotSalary = () => {

		if (this.state.salary) {

			return (
				<div style={{ backgroundColor:'#a5502f' }}>
					<p>
						<p>
							<br />
							<h1 style={{ display: 'flex', justifyContent: 'center', alignItems: 'center' }}>
								You Should Expect {parseInt(this.state.salary)} USD
							</h1>
						</p>
					</p>
				</div>

			);
		} else {
			return (
				<div style={{ backgroundColor:'#a5502f' }}>
					<br />
					<h3 style={{ display: 'flex', justifyContent: 'center', alignItems: 'center' }}>
						Please Fill All fields Before Asking for a Prediction
					</h3>
				</div>
			);
		}
	};

	render() {
		return (
			<div>
				<div style={{ backgroundColor:'#873e23' }}>
					<p>
						<p>
							<br />
							<h1 style={{ display: 'flex', justifyContent: 'center', alignItems: 'center' }}>
								What's My CTC ?
							</h1>
						</p>
					</p>
				</div>
				<form onSubmit={this.handleSubmit} style={{ backgroundColor:'#a5502f' }}>
					<div>
						<p style={{ display: 'flex', justifyContent: 'center', alignItems: 'center' }}>
							<label htmlFor='work_year'>Work Year</label>
							<input style={{ backgroundColor:'#b0e1e6' }}
								name='work_year'
								placeholder='work_year'
								value={this.state.work_year}
								onChange={this.handleChange}
							/>
						</p>
					</div>
					<div>
						<p style={{ display: 'flex', justifyContent: 'center', alignItems: 'center' }}>
							<label htmlFor='employment_type'>Employment Type</label>
							<br />
							<input style={{ backgroundColor:'#b0e1e6' }}
								name='employment_type'
								placeholder='employment_type'
								value={this.state.employment_type}
								onChange={this.handleChange}
							/>
						</p>
					</div>
					<div>
						<p style={{ display: 'flex', justifyContent: 'center', alignItems: 'center' }}>
							<label htmlFor='job_title'>Job Title</label>
							<br />
							<input style={{ backgroundColor:'#b0e1e6' }}
								name='job_title'
								placeholder='job_title'
								value={this.state.job_title}
								onChange={this.handleChange}
							/>
						</p>
					</div>
					<div>
						<p style={{ display: 'flex', justifyContent: 'center', alignItems: 'center' }}>
							<label htmlFor='employee_residence'>Employee Residence</label>
							<br />
							<input style={{ backgroundColor:'#b0e1e6' }}
								name='employee_residence'
								placeholder='employee_residence'
								value={this.state.employee_residence}
								onChange={this.handleChange}
							/>
						</p>
					</div>
					<div>
						<p style={{ display: 'flex', justifyContent: 'center', alignItems: 'center' }}>
							<label htmlFor='remote_ratio'>Remote Ratio</label>
							<br />
							<input style={{ backgroundColor:'#b0e1e6' }}
								name='remote_ratio'
								placeholder='remote_ratio'
								value={this.state.remote_ratio}
								onChange={this.handleChange}
							/>
						</p>
					</div>
					<div>
						<p style={{ display: 'flex', justifyContent: 'center', alignItems: 'center' }}>
							<label htmlFor='company_location'>Company Location</label>
							<br />
							<input style={{ backgroundColor:'#b0e1e6' }}
								name='company_location'
								placeholder='company_location'
								value={this.state.company_location}
								onChange={this.handleChange}
							/>
						</p>
					</div>
					<div>
						<p style={{ display: 'flex', justifyContent: 'center', alignItems: 'center' }}>
							<label htmlFor='company_size'>Company Size</label>
							<br /> 	
							<input style={{ backgroundColor:'#b0e1e6' }}
								name='company_size'
								placeholder='company_size'
								value={this.state.company_size}
								onChange={this.handleChange}
							/>
						</p>
					</div>
					<div style={{ display: 'flex', justifyContent: 'center', alignItems: 'center' }}>
						<button style={{ backgroundColor:'#b0e1e6' }}><h3>What's My CTC ?</h3></button>
					</div>
				</form>
				{this.gotSalary()}
			</div>
		)
	}
}

export default Form
