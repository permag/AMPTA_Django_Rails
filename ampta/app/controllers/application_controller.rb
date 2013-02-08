class ApplicationController < ActionController::Base
  protect_from_forgery
  before_filter :headernav

  def user_logged_in
    # test user id
    session[:user_id] = 1
  end

  def headernav
    @active_user = User.find(self.user_logged_in)
  end
  
  def sidenav
    # get logged in user
    @user = User.find(self.user_logged_in)
    # get projects and tickets for logged in user
    @projects_nav = @user.projects 
    @tickets_nav = @user.tickets.all(:limit => 10)
  end
end
