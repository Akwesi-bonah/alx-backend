it('should display an error message if jobs is not an array', () => {
    expect(() => {
        createPushNotificationsJobs(2, queue);
    }).to.throw('Jobs is not an array');
});

it('should display an error message if jobs array is empty', () => {
    expect(() => {
        createPushNotificationsJobs([], queue);
    }).to.throw('Jobs array is empty');
});

it('should display an error message if jobs array contains non-object elements', () => {
    expect(() => {
        createPushNotificationsJobs([2, 'Hello', null], queue);
    }).to.throw('Jobs array contains non-object elements');
});

it('should create new jobs and add them to the queue', () => {
    createPushNotificationsJobs(jobs, queue);
    expect(queue.testMode.jobs.length).to.equal(2);

    expect(queue.testMode.jobs[0].type).to.equal('push_notification_code_3');
    expect(queue.testMode.jobs[0].data).to.eql({
        phoneNumber: '4153518780',
        message: 'This is the code 1234 to verify your account',
    });

    expect(queue.testMode.jobs[1].type).to.equal('push_notification_code_3');
    expect(queue.testMode.jobs[1].data).to.eql({
        phoneNumber: '4153118782',
        message: 'This is the code 4321 to verify your account',
    });
});