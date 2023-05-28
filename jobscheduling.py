def job_scheduling(jobs):
    jobs.sort(key=lambda x: x[1])  # Sort jobs by finish times
    scheduled_jobs = []
    scheduled_jobs.append(jobs[0])
    for job in jobs[1:]:
        if job[0] >= scheduled_jobs[-1][1]:
            scheduled_jobs.append(job)
    return scheduled_jobs

# jobs = [(1, 3), (2, 5), (4, 7), (6, 9)]
jobs = [(1, 3), (2, 4), (3, 6), (5, 7), (6, 9), (8, 10)]
scheduled_jobs = job_scheduling(jobs)
print(scheduled_jobs)