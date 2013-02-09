class ApplicationController < ActionController::Base
  protect_from_forgery
  before_filter :confirm_logged_in, :except => [:logout]
  before_filter :headernav
  
  def confirm_logged_in
    unless session[:user_id]
      flash[:notice] = "You must be logged in."
      redirect_to :root
      return false
    else
      return true
    end
  end

  def logout
    session[:user_id] = nil
    #redirect_to :action => :root
  end

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
    @projects_nav = @user.projects.order("id DESC")
    @tickets_nav = @user.tickets.order("id DESC").all(:limit => 10)
  end
end
